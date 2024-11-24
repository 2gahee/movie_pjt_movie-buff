<template>
    <h2 class="articles-title">{{ store.userInfo.username }}님의 Articles</h2>
    <div class="btn-table">
    <button @click="goCreate" type="button" class="btn btn-dark">작성하기</button>
        <table class="table table-hover table-striped text-center">
            <thead>
                <tr>
                    <th class="title col-3"><a>제목</a></th>
                    <th class="content col-4"><a>내용</a></th>
                    <th class="created-at"><a>작성일</a></th>
                </tr>
            </thead>
            <tbody>
                <!-- 현재 페이지에 해당하는 게시글만 표시 -->
                <tr v-for="article in paginatedArticles" :key="article.id">
                    <td class="title"><RouterLink :to="{ name: 'articleDetail', params: { id: article.id } }">{{ article.title }}</RouterLink></td>
                    <td class="content">{{ article.content }}</td>
                    <td class="created-at"><time>{{ article.created_at }}</time> </td>
                </tr>
            </tbody>
        </table>
        <!-- 페이지네이션 -->
        <nav id="pagination" aria-label="Page navigation">
            <ul class="pagination justify-content-center">
                <li class="page-item" :class="{ disabled: currentPage === 1 }">
                <button class="page-link" @click="changePage(currentPage - 1)" :disabled="currentPage === 1">이전</button>
                </li>
                <li 
                class="page-item" 
                v-for="page in totalPages" 
                :key="page" 
                :class="{ active: currentPage === page }">
                <button class="page-link" @click="changePage(page)">{{ page }}</button>
                </li>
                <li class="page-item" :class="{ disabled: currentPage === totalPages }">
                <button class="page-link" @click="changePage(currentPage + 1)" :disabled="currentPage === totalPages">다음</button>
                </li>
            </ul>
        </nav>
    </div>
</template>

<script setup>
import { ref, computed, onMounted, watchEffect } from 'vue';
import { useMovieStore } from '@/stores/counter';
import { useRouter } from 'vue-router'
const router = useRouter()
const store = useMovieStore()
const articleList = ref([])
const currentPage = ref(1); 
const itemsPerPage = 10; 
onMounted(() => {
    store.getArticles('username', localStorage.getItem('username'))
})
watchEffect(() => {
    articleList.value = store.articles;
})
const totalPages = computed(() => Math.ceil(articleList.value.length / itemsPerPage));
// 현재 페이지에 표시할 게시글 계산
const paginatedArticles = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return articleList.value.slice(start, end);
});

// 페이지 변경 함수
const changePage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
};
const goCreate = function() {
    router.push({path:'/community/create/'})
}
</script>

<style scoped>
.articles-title {
  margin-top: 2rem;        
  margin-left: 3rem;    
}

table {
 width:80%;
 margin: 0 auto;
}


.btn-table {
 display: flex;
 flex-direction: column;
 align-items: flex-end;
}

.btn {
width: 6rem;
margin-right: 10%;
margin-bottom: 1rem;
}

#pagination{
display: flex;
justify-content: center;
margin-top: 2%;
width: 100%;
}
</style>