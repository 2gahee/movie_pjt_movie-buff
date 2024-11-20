<template>
    <div class="description">
        <h1>굿즈 기반 영화 추천</h1>
        <p>재고 물량이 임박한 영화부터 추천됩니다.</p>
    </div>
    
</template>

<script setup>
import {useRouter } from 'vue-router'
const router = useRouter();

</script>

<style scoped>
    .description{
       margin-top: 2rem; 
       font-weight: bold;
       display: flex;     
       flex-direction: column;
       align-items: center;
    }
</style>