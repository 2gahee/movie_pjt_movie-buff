<template>
    <div class="all">
    <div class="description">
        <h1>게시판</h1>
    </div>
 
   
    <div class="row" id="search-box">
        <div class="card card-margin search-form">
            <div class="card-body p-0">
                <form id="search-form" @submit="searchArticles">
                    <div class="row">
                        <div class="col-12">
                            <div class="search-container">
                                <label for="search-type" hidden>검색 유형</label>
                                    <select class="form-control" id="search-type" name="searchType">
                                        <option>제목</option>
                                        <option>내용</option>
                                        <option>작성자</option>
                                    </select>
                                <label for="search-value" hidden>검색어</label>
                                    <input type="text" placeholder="검색어를 입력해주세요" class="form-control" id="search-value"
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

    <ArticleList />

    <div class="row">
        <nav id="pagination" aria-label="Page navigation">
            <ul class="pagination justify-content-center">
                <li class="page-item"><a class="page-link" href="#">이전</a></li>
                <li class="page-item"><a class="page-link" href="#">1</a></li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
                <li class="page-item"><a class="page-link" href="#">4</a></li>
                <li class="page-item"><a class="page-link" href="#">5</a></li>
                <li class="page-item"><a class="page-link" href="#">다음</a></li>
            </ul>
        </nav>
    </div>
</div>
        
        
	

</template>

<script setup>
import {useRouter } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue';
const router = useRouter();
</script>

<style scoped>
.description{
    margin-top: 2rem; 
    font-weight: bold;
    display: flex;
    justify-content: center;
}

.all {
    min-width: 500px;
}

.search-container{
    display: flex;
}

#search-box{
  min-width: 500px;
  display : inline;
}
.search-form {
  width: 550px;
  margin: 0 auto;
  margin-top: 1rem;  
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



</style>