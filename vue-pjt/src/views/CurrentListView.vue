<template>
    <div>
        <p v-for="movie in nowOnList">{{ movie.title }}</p>
        <MovieCard />
    </div>
</template>

<script setup>
import { ref, onMounted, watchEffect } from 'vue';
import { useMovieStore } from '@/stores/counter';
import MovieCard from '@/components/MovieCard.vue';
// import { useRouter } from 'vue-router'
// const router = useRouter()
const store = useMovieStore()
const nowOnList = ref([])
onMounted(() => {
    store.getNowOns()
})
watchEffect(() => {
    nowOnList.value = store.nowOns;
    console.log(nowOnList.value)
})
</script>

<style scoped>

</style>