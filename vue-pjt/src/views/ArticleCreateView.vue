<template>
  <div>
    <h1>{{ isEditMode ? "게시글 수정" : "게시글 작성" }}</h1>
    <form @submit.prevent="submitArticle">
      <div>
        <label for="title">제목 :</label>
        <input type="text" id="title" v-model.trim="title" />
      </div>
      <div>
        <label for="content">내용 :</label>
        <textarea id="content" v-model.trim="content"></textarea>
      </div>
      <input type="submit" :value="isEditMode ? '수정 완료' : '작성 완료'" />
    </form>
  </div>
</template>


<script setup>
  import { ref, onMounted } from 'vue';
  import { useMovieStore } from '@/stores/counter';
  import { useRoute, useRouter } from 'vue-router';
  import axios from 'axios';

  const store = useMovieStore();
  const route = useRoute();
  const router = useRouter();

  // 폼 상태
  const title = ref('');
  const content = ref('');

  // 수정 모드 확인
  const isEditMode = ref(false);

  // 현재 게시글 ID
  const id = route.params.id;

  // 컴포넌트 초기화 로직
  onMounted(() => {
    // 수정 모드인지 확인 (ID가 있으면 수정 모드)
    isEditMode.value = !!id;

    if (isEditMode.value) {
      // 수정 모드일 경우, 기존 게시글 데이터 불러오기
      fetchArticle();
    }
  });

  // 기존 게시글 데이터를 불러오는 함수
  const fetchArticle = () => {
    axios({
      method: 'get',
      url: `${store.API_URL}/community/${id}/`,
      headers: {
        Authorization: `Token ${store.token}`,
      },
    })
      .then((res) => {
        title.value = res.data.title; // 기존 제목 설정
        content.value = res.data.content; // 기존 내용 설정
      })
      .catch((err) => {
        console.error('게시글 데이터를 불러오는 중 오류 발생:', err);
        alert('게시글 데이터를 불러오지 못했습니다.');
      });
  };

  // 게시글 작성/수정 요청 함수
  const submitArticle = () => {
    if (isEditMode.value) {
      // 수정 모드일 경우
      axios({
        method: 'put',
        url: `${store.API_URL}/community/${id}/`,
        data: {
          title: title.value,
          content: content.value,
        },
        headers: {
          Authorization: `Token ${store.token}`,
        },
      })
        .then(() => {
          alert('게시글이 성공적으로 수정되었습니다.');
          router.push({ name: 'Articles' }); // 게시판 리스트로 이동
        })
        .catch((err) => {
          console.error('게시글 수정 중 오류 발생:', err);
          alert('게시글 수정에 실패했습니다.');
        });
    } else {
      // 작성 모드일 경우
      axios({
        method: 'post',
        url: `${store.API_URL}/community/`,
        data: {
          title: title.value,
          content: content.value,
        },
        headers: {
          Authorization: `Token ${store.token}`,
        },
      })
        .then(() => {
          alert('게시글이 성공적으로 작성되었습니다.');
          router.push({ name: 'Articles' }); // 게시판 리스트로 이동
        })
        .catch((err) => {
          console.error('게시글 작성 중 오류 발생:', err);
          alert('게시글 작성에 실패했습니다.');
        });
    }
  };

</script>
  
<style>
  
</style>
  