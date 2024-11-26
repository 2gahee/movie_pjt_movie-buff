<template>
    <div>
        <div class="description">
            <img src="/images/mypagelogo.png" alt="로고" class="mypagelogo" />
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
.mypagelogo {
  width: 10rem;
  height: auto; 
}

</style>