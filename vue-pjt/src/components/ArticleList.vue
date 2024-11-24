<template>
    <div class="btn-table">
    <!-- <button @click="goTotalList" type="button" class="btn btn-dark">전체 목록</button> -->
    <button @click="goCreate" type="button" class="btn btn-dark">작성하기</button>
    <table class="table table-hover table-striped text-center">
        <thead>
            <tr>
                <th class="title col-5"><a>제목</a></th>
                <!-- <th class="content col-4"><a>내용</a></th> -->
                <th class="username col-3"><a>작성자</a></th>
                <th class="created-at col-2"><a>작성일</a></th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="article in props.articleList" :key="article.id">
                
                <td class="title"> <RouterLink :to="{ name: 'articleDetail', params: { id: article.id } }">{{article.title}}</RouterLink></td>
                <!-- <td class="content">{{article.content}}</td> -->
                <td class="username">{{article.user.username}}</td>
                <td class="created-at">
                    <time>{{article.created_at}}</time>
                </td>
            </tr>
            </tbody>
    </table>
    </div>
</template>

<script setup>


import { useRouter } from 'vue-router'
import { useMovieStore } from '@/stores/counter';
const store = useMovieStore()
const router = useRouter()

const props = defineProps({
    articleList : Array
})
const goCreate = function() {
    router.push({path:'/community/create/'})
}
const goTotalList = function() {
    store.getArticles()
}
</script>

<style scoped>
.btn-table {
 margin-top: 3%;
 display: flex;
 flex-direction: column;
 align-items: center;  
 width: 80%; 
 margin-left: auto; 
 margin-right: auto; 


}

.btn {
width: 6rem;
margin-bottom: 1rem;
align-self: flex-end; 
}

/* 테이블 열 너비 설정 */
th.title, td.title {
    width: 45%;
}

th.username, td.username {
    width: 25%; 
}

th.created-at, td.created-at {
    width: 30%;
}
</style>