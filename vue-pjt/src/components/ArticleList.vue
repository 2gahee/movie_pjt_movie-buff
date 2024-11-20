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
            <tr>
                <td class="title"><a>첫글</a></td>
                <td class="hashtag">#java</td>
                <td class="user-id">Uno</td>
                <td class="created-at">
                    <time>2022-01-01</time>
                </td>
            </tr>
            </tbody>
    </table>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useMovieStore } from '@/stores/counter';
const store = useMovieStore()
onMounted(() => {
    store.getArticles()
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