<template>
  <div class="movie-details-container">
    <div v-if="movie" class="movie-content">
      <div class="movie-header" :style="{ backgroundImage: `url('https://image.tmdb.org/t/p/original/${movie.backdrop_path}')` }">
        <div class="header-overlay">
          <h1 class="movie-title">{{ movie.title }}</h1>
          <div class="movie-metadata">
            <span class="original-title">{{ movie.original_title }}</span>
            <span class="genre-tags">{{ genreString }}</span>
            <div class="movie-stats">
              <span>{{ movie.release_date }}</span>
              <span>{{ Math.floor(movie.runtime / 60) }}시간 {{ movie.runtime % 60 }}분</span>
              <span class="rating">⭐ {{ Math.round(movie.vote_average * 10) / 10 }} ({{ movie.vote_count }}명)</span>
            </div>
          </div>
          <div class="like-section">
            <button 
              v-if="store.token && isLiked != null"
              @click="likeToggle(movie.id)"
              :class="isLiked ? 'btn-liked' : 'btn-like'"
            >
              {{ isLiked ? '좋아요 취소' : '좋아요' }}
            </button>
            <button v-else class="btn-disabled" disabled>로그인 후 좋아요 가능</button>
          </div>
        </div>
      </div>

      <div class="movie-details">
        <div class="poster-container">
          <img 
            :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" 
            alt="Movie Poster" 
            class="movie-poster"
          >
        </div>
        <div class="movie-info">
          <blockquote class="tagline">"{{ movie.tagline }}"</blockquote>
          <p class="overview">{{ movie.overview }}</p>
          <div id="player" v-if="videoId"></div>
        </div>
      </div>
      
      <MovieEvent :title="title"/>

    </div>
    <div v-else class="loading">
      <p>영화 정보를 불러오는 중...</p>
    </div>
  </div>
</template> 

<script setup>
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/counter'
import { onMounted, ref, nextTick } from 'vue'
import MovieEvent from '@/components/MovieEvent.vue';

const store = useMovieStore()
const route = useRoute()
const movie = ref(null)
const genreString = ref('')
const isLiked = ref(null)
const movieId = Number(route.params.id)
const title = ref(null)
const videoId = ref('')
onMounted(async () => {
  if (!movieId || isNaN(movieId)) {
    console.error("유효하지 않은 movieId입니다.")
    return
  }
  
  try {
    movie.value = await store.getMovieDetails(movieId);
    await store.getLikedMovies();
    
    genreString.value = movie.value.genres.map(genre => genre.name).join(" / ");
    title.value = movie.value.title
    videoId.value = await store.getVideoId(title.value)
    if (videoId.value) {
      nextTick(() => {loadYouTubePlayer(videoId.value)
    })}
    const likedMovie = store.likedMovies.find((movie) => movie.id === movieId);
    isLiked.value = !!likedMovie;
  } catch (error) {
    console.error("영화 정보를 가져오는 중 오류 발생:", error);
  }
})

const likeToggle = async function(movieId) {
  try {
    await store.movieLike(movieId)
    isLiked.value = !isLiked.value
  } catch (error) {
    console.error("좋아요 토글 중 오류 발생:", error);
  }
}
function loadYouTubePlayer(videoId) {
  // 이미 로드된 경우, 다시 로드하지 않도록 방지
  if (window.YT && window.YT.Player) {
    new YT.Player('player', {
      height: '360',
      width: '640',
      videoId: videoId,
      events: {
      }
    });
  } else {
    let tag = document.createElement('script')
    tag.src = "https://www.youtube.com/iframe_api"
    let firstScriptTag = document.getElementsByTagName('script')[0]
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag)


  window.onYouTubeIframeAPIReady = function() {
    new YT.Player('player', {
      height: '360',
      width: '640',
      videoId: videoId,
      events: {
      }
    })
  }
}
}
</script>

<style scoped>
.movie-details-container {
  width: 70%;
  margin: 0 auto;
  margin-top: 3rem;
}

.movie-header {
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  color: white;
  position: relative;
  border-radius: 12px;
  overflow: hidden;
}

.header-overlay {
  background: linear-gradient(to right, rgba(0,0,0,0.8), rgba(0,0,0,0.4));
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.movie-title {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.movie-metadata {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.genre-tags {
  color: #cccccc;
}

.movie-stats {
  display: flex;
  gap: 1rem;
  align-items: center;
  color: #eeeeee;
}

.rating {
  color: gold;
  font-weight: bold;
}

.like-section {
  margin-top: 1rem;
}

.btn-like, .btn-liked, .btn-disabled {
  padding: 0.75rem 1.5rem;
  border-radius: 6px;
  font-weight: bold;
  transition: all 0.3s ease;
}

.btn-like {
  background-color: #D72323;
  color: white;
  border: none;
}

.btn-liked {
  background-color: #6c757d;
  color: white;
  border: none;
}

.btn-disabled {
  background-color: #cccccc;
  color: #666666;
  cursor: not-allowed;
}

.movie-details {
  display: flex;
  gap: 2rem;
  margin-top: 2rem;
}

.poster-container {
  width: 30%;
}

.movie-poster {
  width: 100%;
  border-radius: 12px;
  box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}

.movie-info {
  width: 70%;
  margin-top: 1rem;
}

.tagline {
  font-style: italic;
  color: #666;
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.overview {
  line-height: 1.6;
  color: #333;
}

.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 300px;
}


</style>