<template>  
    <div class="card-footer">
        <b>댓글 [{{ comments.length }}]</b>
    </div>
    <div class="list-group">

        <!-- 댓글아이템 -->
        <div class="list-group-item d-flex justify-content-between align-items-center"
        v-for="(comment, index) in comments" 
        :key="index">
            <div class="d-flex">
                <div class="px-1 me-1 bg-dark text-white rounded">{{ comment.user.username }}</div>&nbsp;
                <div>{{ comment.content }}</div>
            </div>
            <div class="ms-auto">{{ comment.created_at }}</div>
            <button v-if="comment.user.username === currentUserName"
             @click="deleteComment(comment.id, index)" 
            class="btn">삭제 </button>   
        </div>
    </div>  
    
</template>

<script setup>
import { defineProps, defineEmits, computed } from 'vue';
import axios from 'axios';
import { useMovieStore } from '@/stores/counter';

const store = useMovieStore();

// 현재 로그인한 사용자의 ID를 스토어에서 가져옴
const currentUserName = computed(() => localStorage.username);


// 부모 컴포넌트로부터 댓글 리스트를 props로 받음
const props = defineProps({
    comments: {
        type: Array,
        required: true,
    },
    id : String,
})

// 부모 컴포넌트에 변경사항을 알리기 위한 emit
const emit = defineEmits(['update:comments']);

const deleteComment = async (commentId, index) => {
  // 사용자 확인
  const confirmDelete = window.confirm('정말로 이 댓글을 삭제하시겠습니까?');
  if (!confirmDelete) return;

  try {
    // DELETE 메서드로 댓글 삭제 요청
    await axios({
      method: 'delete',
      url: `${store.API_URL}/community/${props.id}/${commentId}/`, 
      headers: {
        Authorization: `Token ${store.token}` // 인증 토큰 추가
      }
    });

    // 로컬 배열에서 댓글 제거
    const updatedComments = [...props.comments];
    updatedComments.splice(index, 1);
    
    // 부모 컴포넌트에 업데이트된 댓글 리스트 emit
    emit('update:comments', updatedComments);
  } catch (error) {
    console.error('댓글 삭제 중 오류 발생:', error);
    alert('댓글 삭제에 실패했습니다.');
  }
};


</script>

<style scoped>
.list-group {
  margin-bottom: 2rem;
}
</style>