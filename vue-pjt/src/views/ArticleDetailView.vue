<template>
  <div class="description">
      <h1>게시판</h1>
      <div class="container p-5" v-if="article">


  <!-- 작성자 본인 확인 후, 수정 삭제 버튼 넣기 -->
  <div v-if="article.user.username === currentUsername" class="d-flex justify-content-end">
      <button class="btn btn-warning me-1" @click="goToEditPage">수정</button>
      <button class="btn btn-danger" @click="deleteArticle">삭제</button>
  </div>


  <div class="d-flex justify-content-end mt-2">
      <b>작성자: {{ article.user.username }}</b>&ensp;
      <b>작성일: {{ article.created_at }}</b>&ensp;
      <b>수정일: {{ article.updated_at }}</b>
  </div>

  <!-- 게시글내용 -->
  <div>
      <h3><b>{{ article.title }}</b></h3>
      <hr/>
      <div class="mt-3 p-4" id="contentbox">
          {{ article.content }}
      </div>
  </div>

  <div>
    <button v-show="article.user.username != currentUsername" @click="likeArticle">좋아요</button>
    <p>좋아요 {{ like_count }}개</p>
  </div>
  <!-- 댓글 -->
  <div class="card mt-3">
      <!-- 댓글등록 -->
       <CommentCreate :id="id" @add-comment="addComment"/>
    
      <!-- 댓글목록 -->
       <!-- <CommentList :comments="comments" :id="id" @update:comments="updateComments"/>   -->
       <CommentList :comments="paginatedComments" :id="id" @update:comments="updateComments" />
       <div class="row">
        <nav id="pagination" aria-label="Page navigation">
          <ul class="pagination justify-content-center">
            <li class="page-item">
              <button
                class="page-link"
                :disabled="currentPage === 1"
                @click="changePage(currentPage - 1)"
              >
                이전
              </button>
            </li>
            <li
              class="page-item"
              v-for="page in totalPages"
              :key="page"
              :class="{ active: page === currentPage }"
            >
              <button class="page-link" @click="changePage(page)">{{ page }}</button>
            </li>
            <li class="page-item">
              <button
                class="page-link"
                :disabled="currentPage === totalPages"
                @click="changePage(currentPage + 1)"
              >
                다음
              </button>
            </li>
          </ul>
        </nav>
    </div>     
  </div>
</div>

  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, computed } from 'vue';
import { useMovieStore } from '@/stores/counter';
import { useRoute, useRouter } from 'vue-router'
import CommentList from '@/components/CommentList.vue';
import CommentCreate from '@/components/CommentCreate.vue';

const route = useRoute()
const router = useRouter();
const store = useMovieStore()
const like_count = ref(null)
const article = ref(null)
const comments = ref([]); // 댓글 리스트 상태

const id = route.params.id //현재 게시글 id
const currentPage = ref(1);
const itemsPerPage = 10;
const currentUsername = localStorage.username || '';// 현재 로그인된 사용자 이름

// 댓글 페이지네이션 관련 계산 속성
const totalPages = computed(() => Math.ceil(comments.value.length / itemsPerPage));
const paginatedComments = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return comments.value.slice(start, end); // 현재 페이지에 해당하는 댓글만 반환
});

// 페이지 변경 함수
const changePage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
};

// 새 댓글을 추가하는 함수
const addComment = (newComment) => {
  comments.value.push(newComment); 
};


const updateComments = (newComments) => {
comments.value = newComments;
};

// DetailView가 마운트되기전에 DRF로 단일 게시글 조회를 요청 후 응답데이터를 저장
onMounted(() => {
axios({
  method: 'get',
  url: `${store.API_URL}/community/${id}/`,
  headers: {
    Authorization: `Token ${store.token}` // 인증 토큰 추가
  }
})
  .then((res) => {
    console.log(res.data)
    article.value = res.data
    comments.value = res.data.comment_set || []; // 댓글 데이터를 받아 저장(존재하지 않으면 빈 배열)
    like_count.value = res.data.like_users.length
  })
  .catch((err) => {
    console.log(err)
  })
})


// 게시글 삭제
const deleteArticle = () => {
const confirmDelete = window.confirm('정말로 이 게시글을 삭제하시겠습니까?');
if (!confirmDelete) return;

axios({
  method: 'delete',
  url: `${store.API_URL}/community/${id}/`,
  headers: {
    Authorization: `Token ${store.token}`, // 인증 토큰 추가
  },
})
  .then(() => {
    alert('게시글이 삭제되었습니다.');
    router.push('/community'); // 게시판 리스트로 이동
  })
  .catch((err) => {
    console.error(err);
    alert('게시글 삭제에 실패했습니다.');
  });
};

const likeArticle = () => {
  axios({
  method: 'put',
  url: `${store.API_URL}/community/${id}/like/`,
  headers: {
    Authorization: `Token ${store.token}` // 인증 토큰 추가
  }
})
  .then((res) => {
    console.log(res.data)
    like_count.value = res.data.like_users.length
  })
  .catch((err) => {
    console.log(err)
  })
}

// 수정 페이지로 이동(수정 전용 라우트로 이동)
const goToEditPage = () => {
router.push({ name: 'editArticle', params: { id } }); //해당 게시글 ID 라우터에 전달
};

</script>

<style scoped>
.description{
     margin-top: 2rem; 
     font-weight: bold;
     display: flex;     
     flex-direction: column;
     align-items: center;
  }
  #contentbox{
      background-color: #FFFF;
      height: auto;
      min-height: 10rem;

  }

</style>