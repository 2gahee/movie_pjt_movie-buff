<template>
    <div class="all">
    <div class="description">
      <img src="/images/articlelogo.png" alt="로고" class="articlelogo" />
    </div>
   
    <div class="row" id="search-box">
        <div class="card card-margin search-form">
            <div class="card-body p-0">
                <form id="search-form" @submit.prevent="searchArticles">
                    <div class="row">
                        <div class="col-12">
                            <div class="search-container">
                                <label for="search-type" hidden>검색 유형</label>
                                    <select class="form-control" id="search-type" name="searchType">
                                        <option value="title">제목</option>
                                        <option value="content">내용</option>
                                        <option value="username">작성자</option>
                                    </select>
                                <label for="search-value" hidden>검색어</label>
                                    <input v-model="query" type="text" placeholder="검색어를 입력해주세요" class="form-control" id="search-value"
                                           name="searchValue">
                                <button type="submit" class="btn btn-base">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                                             viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                             stroke-linecap="round" stroke-linejoin="round"
                                             class="feather feather-search">
                                            <circle cx="11" cy="11" r="8"></circle>
                                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                                        </svg>
                                    </button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
    
    <ArticleList :articleList="paginatedArticles" />

    <div class="row">
      <nav id="pagination" aria-label="Page navigation">
        <ul class="pagination justify-content-center">
          <li class="page-item">
            <button
              class="page-link"
              :disabled="currentPage === 1"
              @click="changePage(currentPage - 1)"
            >
              이전
            </button>
          </li>
          <li
            class="page-item"
            v-for="page in totalPages"
            :key="page"
            :class="{ active: page === currentPage }"
          >
            <button class="page-link" @click="changePage(page)">{{ page }}</button>
          </li>
          <li class="page-item">
            <button
              class="page-link"
              :disabled="currentPage === totalPages"
              @click="changePage(currentPage + 1)"
            >
              다음
            </button>
          </li>
        </ul>
      </nav>
    </div>

</div>       
</template>

<script setup>
import { ref, computed, onMounted, watchEffect } from 'vue';
import { useMovieStore } from '@/stores/counter';
import ArticleList from '@/components/ArticleList.vue';
const store = useMovieStore()
const articleList = ref([])
const currentPage = ref(1);
const itemsPerPage = 9;
const query = ref('')
onMounted(() => {
    store.getArticles()
})
// pagination
const totalPages = computed(() => Math.ceil(articleList.value.length / itemsPerPage));
const paginatedArticles = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return articleList.value.slice(start, end);
});

const changePage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
}



const searchArticles = function() {
    const field = document.querySelector('#search-type').value
    store.getArticles(field, query.value)
    query.value = ''
}
watchEffect(() => {
    articleList.value = store.articles;
})

</script>

<style scoped>
body, html {
    margin: 0;
    padding: 0;
    overflow-x: hidden; /* 가로 스크롤 제거 */
}

.description{
    margin-top: 2rem; 
    font-weight: bold;
    display: flex;
    justify-content: center;
}

.articlelogo {
  width: 10rem;
  height: auto; 
}

.search-container{
    display: flex;
}

#search-box{
  width: 400px;
  display : inline;
}
.search-form {
  width: 550px;
  margin: 0 auto;
}

.search-form input {
  height: 100%;
  border: 0;
  display: block;
  width: 400px;
  padding: 1rem;
  height: 100%;
  font-size: 1rem;
  margin: auto;
}

.search-form select {
  background: transparent;
  border: 0;
  padding: 1rem;
  height: 100%;
  width: 80px;
  font-size: 1rem;
  margin: auto;
}

.search-form select:focus {
  border: 0;
}

.search-form button {
  height: 100%;
  width: 50px;
  margin: auto;
}

#search-type {
  margin-right:4px;
}

#pagination{
    margin-top: 2%;
}

.like-section {
  display: flex;
  justify-content: flex-end;
  align-items: baseline;
  gap: 10px;
  margin-top: 1rem;
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

</style>