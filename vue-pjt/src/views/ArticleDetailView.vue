<template>
    <div class="description">
        <h1>게시판</h1>
        <div class="container p-5" v-if="article">


    <!-- 나중에 마이페이지 내가쓴 게시글에서 수정 삭제 아래 버튼 넣기 -->
        <!-- <div class="d-flex justify-content-end">
            <button class="btn btn-warning me-1">수정</button>
            <button class="btn btn-danger">삭제</button>
        </div> -->

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

    <!-- 댓글 -->
    <div class="card mt-3">
        <!-- 댓글등록 -->
         <CommentCreate :id="id" @add-comment="addComment"/>
      
        <!-- 댓글목록 -->
         <CommentList :comments="comments" :id="id" @update:comments="updateComments"/>       
    </div>
</div>

    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue';
import { useMovieStore } from '@/stores/counter';
import { useRoute } from 'vue-router'
import CommentList from '@/components/CommentList.vue';
import CommentCreate from '@/components/CommentCreate.vue';

const route = useRoute()
const store = useMovieStore()

const article = ref(null)
const comments = ref([]); // 댓글 리스트 상태
const id = route.params.id

// 새 댓글을 추가하는 함수
const addComment = (newComment) => {
    comments.value.push(newComment); // 새 댓글을 리스트에 추가
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

    })
    .catch((err) => {
      console.log(err)
    })
})




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