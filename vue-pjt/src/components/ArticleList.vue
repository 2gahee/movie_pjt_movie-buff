<template>

    <div class="btn-table">
    <button type="button" class="btn btn-dark">작성하기</button>
    <table class="table table-hover table-striped text-center">
        <thead>
            <tr>
                <th class="title col-3"><a>제목</a></th>
                <th class="hashtag col-4"><a>내용</a></th>
                <th class="user-id"><a>작성자</a></th>
                <th class="created-at"><a>작성일</a></th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="article in articleList" :key="article.pk">
                <td class="title"><a>{{article.title}}</a></td>
                <td class="hashtag">{{article.content}}</td>
                <td class="user-id">{{article.user_id}}</td>
                <td class="created-at">
                    <time>{{article.created_at}}</time>
                </td>
            </tr>
            </tbody>
    </table>
    </div>
</template>

<script setup>
import { ref, onMounted, watchEffect } from 'vue';
import { useMovieStore } from '@/stores/counter';
const store = useMovieStore()
const articleList = ref([])
onMounted(() => {
    store.getArticles()
})
watchEffect(() => {
    articleList.value = store.articles;
})
</script>

<style scoped>
table {
 width:80%;
 margin: 0 auto;
}


.btn-table {
 margin-top: 3%;
 display: flex;
 flex-direction: column;
 align-items: flex-end;
}

.btn {
width: 6rem;
margin-right: 10%;
margin-bottom: 1rem;
}
</style>