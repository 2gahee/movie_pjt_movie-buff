import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
export const useMovieStore = defineStore('movie', () => {
 //여러개의 컴포넌트에서 활용하는 데이터만 store로 관리
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/community`
    })
    .then(res => {
      console.log(res.data)
    })
    .catch(err => console.log(err))
  }
  return { articles, API_URL, getArticles }
})
