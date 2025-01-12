<template>
    <div v-if="articleList.length === 0" class="no-articles">
        <p>작성하신 게시글이 없습니다. 게시글을 작성해보세요!</p>
        <button @click="goCreate" type="button" class="btn btn-dark">작성하기</button>
    </div>
    <div v-else class="btn-table">
    <button @click="goCreate" type="button" class="btn btn-dark">작성하기</button>
        <table class="table table-hover table-striped text-center">
            <thead>
                <tr>
                    <th class="title col-4"><a>제목</a></th>
                    <th class="created-at col-4"><a>작성일</a></th>
                     <th class="content col-3"><a>좋아요수</a></th>
                </tr>
            </thead>
            <tbody>
                <!-- 현재 페이지에 해당하는 게시글만 표시 -->
                <tr v-for="article in paginatedArticles" :key="article.id">
                    <td class="title"><RouterLink class='link' :to="{ name: 'articleDetail', params: { id: article.id } }">{{ article.title }} [{{ article.comment_count }}]</RouterLink></td>
                    <td class="created-at"><time>{{ article.created_at }}</time> </td>
                    <td class="likes">{{ article.like_users.length }}</td>
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

.btn-table {
 margin-top: 1%;
 display: flex;
 flex-direction: column;
 align-items: center;  
 width: 95%; 
 margin-left: auto; 
 margin-right: auto; 
 margin-bottom: 4rem;
}


.btn {
width: 6rem;
margin-bottom: 1rem;
align-self: flex-end; 
}

#pagination{
display: flex;
justify-content: center;
margin-top: 2%;
width: 100%;
}

.pagination {
  background-color: transparent; 
}

.page-link {
  color: #6c757d; 
  background-color: #f8f9fa; 
  border: 1px solid #dee2e6; 
  transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out; 
}

.page-link:hover {
  color: #ffffff; 
  background-color: #343a40; 
  border-color: #343a40; 
}

.page-item.active .page-link {
  color: #ffffff; 
  background-color: #212529; 
  border-color: #212529; 
  font-weight: bold; 
}

.page-item.disabled .page-link {
  color: #adb5bd; 
  background-color: #e9ecef; 
  border-color: #dee2e6; 
}

.no-articles {
  text-align: center;
  margin-top: 2rem;
  margin-left: 3rem;
 
}

.no-articles p {
  font-size: 1.2rem;
  margin-bottom: 1rem;
}

.link {
    text-decoration: none;  
    color: black;  
}

.link:hover {
    color: #333;
}


</style>