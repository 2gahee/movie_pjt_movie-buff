<template>
    <!-- 댓글등록 -->
    <div class="card-body">
        <textarea class="form-control" rows="2" name="comment" placeholder="댓글을 입력하세요" v-model="commentContent"></textarea>
        <div class="d-flex justify-content-end">
            <button class="btn btn-dark mt-1" @click="submitComment">댓글등록</button>
        </div>
    </div>
     
</template>

<script setup>
import axios from 'axios'
import { useMovieStore } from '@/stores/counter';
import { ref, defineEmits } from 'vue';

const store = useMovieStore()
const props = defineProps({
    id: String
})

// 이벤트 emit 정의
const emit = defineEmits(['add-comment']);
const commentContent = ref('');

// 댓글 등록 함수
const submitComment = () => {
  if (!commentContent.value.trim()) {
    alert('댓글을 입력해주세요.');
    return;
  }
  // 새로운 댓글 객체 생성
    axios({
      method: 'post',
      url: `${store.API_URL}/community/${props.id}/comments/`,
      data: {
        content: commentContent.value
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) => {
            console.log('댓글 작성 성공!', res.data);
            // 부모 컴포넌트로 새 댓글 데이터 전달
            emit('add-comment', res.data);
            commentContent.value = '';
      })
      .catch((err) => {
        console.log(err)
      })
};

</script>

<style scoped>
.form-control {
  height: 15rem;
}
</style>