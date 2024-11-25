<template>
   <h2 class="accountinfo-title">{{ store.userInfo.username }}님의 AccountInfo</h2>
  <div class="mypage-container">
      <div class="profile-card">
          <div class="profile-header">
              <h2>{{ store.userInfo.username }} 님의 회원 정보</h2>
              <div class="profile-actions">
                  <router-link to="/editprofile" class="edit-button">
                      정보 수정
                  </router-link>
              </div>
          </div>

          <div v-if="store.userInfo" class="profile-content">
              <div class="info-section">
                  <div class="info-item">
                      <span class="label">아이디</span>
                      <span class="value">{{ store.userInfo.username }}</span>
                  </div>
                  <div class="info-item">
                      <span class="label">닉네임</span>
                      <span class="value">{{ store.userInfo.nickname }}</span>
                  </div>
                  <div class="info-item">
                      <span class="label">이메일</span>
                      <span class="value">{{ store.userInfo.email }}</span>
                  </div>
                  <div class="info-item">
                      <span class="label">비밀번호</span>
                      <span class="value">{{ store.userInfo.password }}</span>
                  </div>
              </div>
          </div>
          <div v-else class="loading">
              <p>정보를 불러오는 중입니다.</p>
          </div>
      </div>
  </div>
</template>


<script setup>
import { onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter';

const store = useMovieStore()

// 페이지가 로드될 때 사용자 정보 조회
onMounted(() => {
  store.fetchUserInfo()
})



</script>

<style scoped>
.accountinfo-title {
  margin-top: 5rem;        
  margin-left: 3rem; 
  margin-bottom: 3rem;   
}

.mypage-container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 0 1rem;
}

.profile-card {
    background: white;
    border-radius: 16px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    overflow: hidden;
}

.profile-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem 2rem;
    border-bottom: 1px solid #eef0f5;
}

.profile-header h2 {
    font-size: 1.5rem;
    font-weight: 600;
    color: #2c3e50;
    margin: 0;
}

.edit-button {
    display: inline-block;
    padding: 0.6rem 1.2rem;
    background-color: #3498db;
    color: white;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 500;
    transition: background-color 0.2s;
}

.edit-button:hover {
    background-color: #2980b9;
}

.profile-content {
    padding: 2rem;
}

.info-section {
    display: grid;
    gap: 1.5rem;
}

.info-item {
    display: flex;
    align-items: center;
    padding: 1rem 1.5rem;
    background: #f8f9fa;
    border-radius: 12px;
}

.label {
    flex: 0 0 100px;
    font-size: 0.95rem;
    color: #6c757d;
}

.value {
    color: #2c3e50;
    font-weight: 500;
}

.loading {
    padding: 2rem;
    text-align: center;
    color: #6c757d;
}

@media (max-width: 640px) {
    .mypage-container {
        margin: 1rem;
    }

    .profile-header {
        padding: 1rem 1.5rem;
        flex-direction: column;
        gap: 1rem;
        text-align: center;
    }

    .info-item {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.5rem;
    }

    .label {
        flex: none;
    }
}

</style>