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
        <div class="card-body">
            <form action="/reply/save" method="post">
                <textarea class="form-control" rows="2" name="comment"></textarea>
                <div class="d-flex justify-content-end">
                    <button type="submit" class="btn btn-outline-primary mt-1">댓글등록</button>
                </div>
            </form>
        </div>
        <!-- 댓글목록 -->

        <div class="card-footer">
            <b>댓글리스트</b>
        </div>
        <div class="list-group">

            <!-- 댓글아이템 -->
            <div class="list-group-item d-flex justify-content-between align-items-center">
                <div class="d-flex">
                    <div class="px-1 me-1 bg-primary text-white rounded">cos</div>
                    <div>댓글 내용입니다</div>
                </div>
                <!-- <form action="/reply/1/delete" method="post">
                    <button class="btn">🗑</button>
                </form> -->
            </div>
            <!-- 댓글아이템 -->
            <div class="list-group-item d-flex justify-content-between align-items-center">
                <div class="d-flex">
                    <div class="px-1 me-1 bg-primary text-white rounded">ssar</div>
                    <div>댓글 내용입니다</div>
                </div>
                <!-- <form action="/reply/1/delete" method="post">
                    <button class="btn">🗑</button>
                </form> -->
            </div>
        </div>
    </div>
</div>

    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue';
import { useMovieStore } from '@/stores/counter';
import { useRoute } from 'vue-router'
const route = useRoute()
const store = useMovieStore()
const article = ref(null)

// DetailView가 마운트되기전에 DRF로 단일 게시글 조회를 요청 후 응답데이터를 저장
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/community/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}` // 인증 토큰 추가
    }
  })
    .then((res) => {
      console.log(res.data)
      article.value = res.data
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