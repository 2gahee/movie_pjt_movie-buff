<template>
    <div>
        <div class="description">
            <img src="/images/nowonlogo.png" alt="로고" class="nowonlogo" />
        </div>
        <div class="MovieCardContainer">
        <MovieCard v-for="movie in nowOnList" :key="movie.id" @click="watchDetail(movie.id)" :movie="movie"/>
        </div>
    </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter'
import MovieCard from '@/components/MovieCard.vue'
import { useRouter } from 'vue-router'
const router = useRouter()
const store = useMovieStore()

onMounted(async function() {
    await store.getNowOns()
})
const nowOnList = computed(() => store.nowOns)
const watchDetail = function(id) {
    router.push({name:'detail', params: {id}})
}
</script>

<style scoped>
.description{
    margin-top: 2rem; 
    margin-bottom: 2rem;
    font-weight: bold;
    display: flex;
    justify-content: center;
}
.MovieCardContainer{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
.nowonlogo {
  width: 10rem;
  height: auto; 
}
</style>