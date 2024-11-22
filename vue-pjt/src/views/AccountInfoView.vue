<template>
    <div>
        <h1>Account Info</h1>
        <h2>내 프로필</h2>
        <div v-if="store.userInfo.username">
        <div>
            <label for="username">Username:</label>
            <input v-model="store.userInfo.username" id="username" type="text" />
        </div>
        <div>
            <label for="nickname">Nickname:</label>
            <input v-model="store.userInfo.nickname" id="nickname" type="text" />
        </div>
        <div>
            <label for="email">Email:</label>
            <input v-model="store.userInfo.email" id="email" type="email" />
        </div>
        <div>
            <label for="password">Password:</label>
            <input v-model="store.userInfo.password" id="password" type="password" />
        </div>
        <button @click="updateProfile">정보 수정</button>
        </div>
        <div v-else>
        <p>사용자 정보를 불러오는 중...</p>
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

// 사용자 정보 수정
const updateProfile = () => {
  const updatedInfo = {
    username: store.userInfo.username,
    nickname: store.userInfo.nickname,
    email: store.userInfo.email,
    password: store.userInfo.password,
  }
  store.updateUserInfo(updatedInfo)
}
</script>

<style scoped>

</style>