<template>
    <div>
        <div class="description">
        <h1>Movies</h1>
        </div>
        <div class="row" id="search-box">
        <div class="card card-margin search-form">
            <div class="card-body p-0">
                <form id="search-form" @submit.prevent="searchMovies">
                    <div class="row">
                        <div class="col-12">
                            <div class="search-container">
                                <label for="search-type" hidden>검색 유형</label>
                                    <select class="form-control" id="search-type" name="searchType">
                                        <option value="title">제목</option>
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
        <div class="MovieCardContainer">
        <MovieCard v-for="movie in movieList" :key="movie.id" @click="watchDetail(movie)" :movie="movie"/>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter'
import MovieCard from '@/components/MovieCard.vue'
import { useRouter } from 'vue-router'
const router = useRouter()
const store = useMovieStore()
const query = ref('')
onMounted(async function() {
    await store.getMoviePicks()
})
const searchMovies = async function() {
    if (query.value.trim()) {
        await store.searchMovies(query.value) 
    }
}
const movieList = computed(() => store.movies)
const watchDetail = function(movie) {
    const movieId = movie.movie_id || movie.id
    router.push({name:'detail', params: {id : movieId}})
}
</script>

<style scoped>
.MovieCardContainer{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
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
</style>