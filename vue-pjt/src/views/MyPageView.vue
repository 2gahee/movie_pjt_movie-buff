<template>
     <div class="description">
        <img src="/images/mypagelogo.png" alt="로고" class="mypagelogo" />
    </div>
    
    <div class="mypage-container">
      <!-- 탭 네비게이션 -->
      <nav class="tabs">
        <button
          class="tab-btn"
          :class="{ active: activeTab === 'myArticle' }"
          @click="changeTab('myArticle')"
        >
          My Articles
        </button>
        <button
          class="tab-btn"
          :class="{ active: activeTab === 'myMovies' }"
          @click="changeTab('myMovies')"
        >
          My Movies
        </button>
        <button
          class="tab-btn"
          :class="{ active: activeTab === 'accountInfo' }"
          @click="changeTab('accountInfo')"
        >
          Account Info
        </button>
      </nav>
  
      <!-- 탭 컨텐츠 -->
      <div v-if="activeTab === 'myArticle'" class="tab-content">
        <AccountArticles/>
      </div>
      <div v-if="activeTab === 'myMovies'" class="tab-content">
        <AccountMovieLikes/>
      </div>
      <div v-if="activeTab === 'accountInfo'" class="tab-content">
        <AccountInfoView/>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import AccountArticles from '@/components/AccountArticles.vue';
  import AccountMovieLikes from '@/components/AccountMovieLikes.vue';
  import AccountInfoView from './AccountInfoView.vue';
  
  const activeTab = ref('myArticle'); // 기본 활성 탭 설정
  
  const changeTab = (tab) => {
    console.log('Tab changed to:', tab);
    activeTab.value = tab; // 활성 탭 변경
  };
  </script>
  
  <style scoped>
  .mypage-container {
    margin: 2rem auto;
    width: 65%;
  }
  
  .tabs {
    display: flex;
    justify-content: space-around;
    margin-bottom: 1rem;
    border-bottom: 2px solid #dee2e6;
  }
  
  .tab-btn {
    padding: 1rem 1.5rem;
    background: none;
    border: none;
    font-size: 1.2rem;
    font-weight: 500;
    color: #6c757d;
    cursor: pointer;
    transition: color 0.3s, border-color 0.3s;
    border-bottom: 2px solid transparent;
  }
  
  .tab-btn:hover {
    color: #212529;
  }
  
  .tab-btn.active {
    color: #212529;
    font-weight: bold;
    border-bottom: 2px solid #212529;
  }
  .description{
    margin-top: 2rem; 
    font-weight: bold;
    }
    .mypagelogo {
    width: 10rem;
    height: auto; 
    }
  </style>
  