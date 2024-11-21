import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'



export const useMovieStore = defineStore('movie', () => {
  const articles = ref([])
  const nowOns = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const likedMovies = ref([])
  // const token = ref(null)

  // const isLogin = computed(() => {
  //   if (token.value === null) {
  //     return false
  //   } else {
  //     return true
  //   }
  // })

  // 페이지 새로고침 시 토큰 복원
  const savedToken = localStorage.getItem('token') || null
  const token = ref(savedToken)

  const isLogin = computed(() => token.value !== null)

  const router = useRouter()

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/community`,
      headers: {
        Authorization: `Token ${token.value}`
        // Accept: 'application/json'
      },
      withCredentials: true
    })
    .then(res => {
      articles.value = res.data
      console.log(res.data)
      
    })
    .catch(err => console.log(err))
  }

const signUp = function (payload) {
  const { username, password1, password2, nickname, email } = payload

  axios({
    method:'post',
    url: `${API_URL}/accounts/signup/`,
    withCredentials: true,
    data: {
      username, password1, password2, nickname, email
    }
  })
    .then((res) => {
      if (res.data) {
        console.log('회원가입 성공:', res.data);
        const password = password1
        logIn({ username, password })
      } else {
        console.error('응답 데이터 없음');
      }

    })
    .catch((error) => {
      // console.error(error.response)
      console.error('Error response:', error.response);
      if (error.response && error.response.data) {
        console.error('Error details:', error.response.data);
        // non_field_errors가 있을 경우 그 내용을 확인
        if (error.response.data.non_field_errors) {
          console.error('Non-field errors:', error.response.data.non_field_errors);
        }
      }

  })
}


const logIn = function (payload) {
  const { username, password } = payload

  axios({
    method: 'post',
    url: `${API_URL}/accounts/login/`,
    data: {
      username, password
    }
  })
    .then((res) => {
      token.value = res.data.key
      localStorage.setItem('token', token.value) // 로그인 시 토큰 저장
      router.push({ name: 'Home' })
      console.log(res.data)
      console.log('로그인 성공')
    })
    .catch((err) => {
      console.log(err)
    })
}

const logOut = function () {
  token.value = null
  localStorage.removeItem('token') // 로그아웃 시 토큰 삭제
  router.push({ name: 'Home' })
}


const getNowOns = async function () {
  try {
    const headers = token.value
    ? { Authorization: `Token ${token.value}` } // 로그인 상태
    : {}; // 비로그인 상태
    
    const res = await axios({
      method: 'get',
      url: `${API_URL}/movies/now-on/`,
      headers: headers,
      withCredentials: true
    })
    nowOns.value = res.data
  } catch (error) {
    console.error("현재 상영작 정보를 가져오는 중 오류:", error)
}}

const getMovieDetails = async function(movieId) {
  try {
      const res = await axios({
          method: 'get',
          url: `${API_URL}/movies/${movieId}/`,
          headers: {
              Authorization: `Token ${token.value}`,
          },
          withCredentials: true,
      });
      console.log('API 응답');
      return res.data
  } catch (err) {
      console.error("API 요청 중 오류 발생:", err)
      throw err
  }
}

const movieLike = function(id, event) {
  try {
    event.preventDefault()
    axios({
      method: 'post',
      url: `${API_URL}/movies/${id}/like/`,
      headers: {
          Authorization: `Token ${token.value}`,
      },
      withCredentials: true,
    })
    console.log('좋아요 토글');
} catch (err) {
    console.error("좋아요 토글 중 오류 발생:", err)
    throw err
}
}

const getLikedMovies = async function () {
  try {
    const res = await axios({
      method: 'get',
      url: `${API_URL}/movies/liked_movies/`,
      headers: { Authorization: `Token ${token.value}` },
      withCredentials: true
    })
    likedMovies.value = res.data.liked_list
  } catch (error) {
    console.error("사용자 영화정보 가져오는 중 오류:", error)
}}
  return { articles, API_URL, getArticles, signUp, logIn, logOut, token,
    getNowOns, isLogin, nowOns, getMovieDetails, movieLike, savedToken, getLikedMovies, likedMovies}
})
