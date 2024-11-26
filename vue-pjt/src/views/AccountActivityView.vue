<template>
    <div>
        <div class="description">
        <h1>My Activities</h1>
        </div>
        <AccountArticles />
        <AccountMovieLikes />
        
    </div>
</template>

<script setup>
import AccountArticles from '@/components/AccountArticles.vue';
import AccountMovieLikes from '@/components/AccountMovieLikes.vue'


</script>

<style scoped>
.description{
    margin-top: 2rem; 
    font-weight: bold;
}
</style>