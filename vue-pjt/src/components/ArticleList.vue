<template>
    <div class="btn-table">
    <!-- <button @click="goTotalList" type="button" class="btn btn-dark">전체 목록</button> -->
    <button @click="goCreate" type="button" class="btn btn-dark">작성하기</button>
    <table class="table table-hover table-striped text-center">
        <thead>
            <tr>
                <th class="title col-3"><a>제목</a></th>
                <th class="username col-2"><a>작성자</a></th>
                <th class="created-at col-3"><a>작성일</a></th>
                <th class="comments col-2"><a>좋아요 수</a></th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="article in props.articleList" :key="article.id">
                <td class="title"> <RouterLink :to="{ name: 'articleDetail', params: { id: article.id } }">{{article.title}} [{{ article.comment_count }}]</RouterLink></td>
                <td class="username">{{article.user.username}}</td>
                <td class="created-at"><time>{{article.created_at}}</time></td>
                <td class="likes">{{ article.likes_count }}</td>
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
/* background-color: #007bff; */
color: #FFFF;
}
</style>