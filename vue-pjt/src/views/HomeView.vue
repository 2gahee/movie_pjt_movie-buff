<template>
    <div class="home-description">
        <h1>무비덕후 영화 추천</h1>
        <p>갱신 버튼을 누르면 굿즈 재고를 기반으로 영화를 추천드려요!</p>
        <button class="btn btn-primary btn-lg" @click.prevent="goodsRecommend">갱신</button>
        <div v-if="bestRecommend" id="carouselAutoplaying" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-indicators">
                <button type="button" data-bs-target="#carouselAutoplaying" data-bs-slide-to="0" class="active" aria-current="true"></button>
                <button v-for="(movie, index) in recommendList" type="button" data-bs-target="#carouselAutoplaying" :data-bs-slide-to=(index+1) ></button>
            </div>
        <div class="carousel-inner">
            <div class="carousel-item active" @click="watchDetail(bestRecommend.id)">
            <img :src=imgString(bestRecommend) class="d-block w-100" alt="...">
            <div class="carousel-caption d-none d-md-block">
                <p>{{ bestRecommend.title }}</p>
                </div>
            </div>
            <div v-for="movie in recommendList" class="carousel-item" @click="watchDetail(movie.id)">
                <img :src=imgString(movie) class="d-block w-100" alt="...">
                <div class="carousel-caption d-none d-md-block">
                    <p>{{ movie.title }}</p>
                </div>
            </div>  
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselAutoplaying" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselAutoplaying" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
        </div>
        <div v-else>Error while loading</div>
    </div>
    
</template>

<script setup>
import { onMounted, computed } from 'vue';
import { useMovieStore } from '@/stores/counter';
import { useRouter } from 'vue-router'
const router = useRouter();
const store = useMovieStore()


onMounted(async function() {
    await store.getNowOns()
})
const wholeRecommendList = computed(() => store.nowOns)
const bestRecommend = computed(() => wholeRecommendList.value.slice(0,1)[0])
const recommendList = computed(() => wholeRecommendList.value.slice(1, 5))
const watchDetail = function(id) {
    router.push({name:'detail', params: {id}})
}
const imgString = function(movie) {
    return `https://image.tmdb.org/t/p/original${movie.backdrop_path}`
}
const goodsRecommend = async function() {
    await store.getEvents()
    if (store.eventList && store.eventList.length) {
        console.log(store.eventList)
        localStorage.setItem("megabox", JSON.stringify(store.eventList))
    }
}
</script>

<style scoped>
.home-description{
   margin-top: 2rem; 
   font-weight: bold;
   display: flex;     
   flex-direction: column;
   align-items: center;
}
.carousel-caption{
    font-size : 30px;
    font-weight : bold;
    color: white;
    text-align: left;
}
</style>

<!-- <script setup>
import { ref, computed } from 'vue';
import { useMovieStore } from '@/stores/counter';

const store = useMovieStore();
const isNowOn = ref(true); // 현재 상태 (true: nowOns, false: eventList)
const loading = ref(false); // 로딩 상태
const displayList = ref([]); // 현재 표시할 리스트

// 초기 nowOns 리스트 가져오기
const fetchNowOns = async () => {
    loading.value = true;
    await store.getNowOns();
    displayList.value = store.nowOns;
    loading.value = false;
};

// 이벤트 리스트 가져오기
const fetchEventList = async () => {
    loading.value = true;
    await store.getEvents();
    displayList.value = store.eventList;
    loading.value = false;
};

// 토글 함수
const toggleNowons = async () => {
    if (loading.value) return; // 이미 로딩 중일 경우 중복 호출 방지
    isNowOn.value = !isNowOn.value;

    if (isNowOn.value) {
        await fetchNowOns();
    } else {
        await fetchEventList();
    }
};

// 슬라이드 추천 리스트
const recommendList = computed(() => displayList.value.slice(1, 5)); // 슬라이드에 표시할 데이터

// 컴포넌트 초기화 시 초기 리스트 설정
fetchNowOns();
</script>

<template>
    <div class="home-description">
        <h1>무비덕후 영화 추천</h1>
        <p>갱신 버튼을 누르면 굿즈 재고를 기반으로 영화를 추천드려요!</p>

        <button class="btn btn-primary btn-lg" @click="toggleNowons">
            {{ isNowOn ? "이벤트 보기" : "현재 상영작 보기" }}
        </button>

        <!-- 로딩 상태 표시 -->
        <!-- <div v-if="loading" class="loading-spinner">
            로딩 중...
        </div> -->

        <!-- 리스트 렌더링 -->
        <!-- <div v-else-if="displayList.length">
            <div id="carouselAutoplaying" class="carousel slide" data-bs-ride="carousel">
                <div class="carousel-indicators">
                    <button type="button" data-bs-target="#carouselAutoplaying" data-bs-slide-to="0" class="active" aria-current="true"></button>
                    <button v-for="(movie, index) in recommendList" :key="index" type="button" data-bs-target="#carouselAutoplaying" :data-bs-slide-to="index + 1"></button>
                </div>
                <div class="carousel-inner">
                    <div v-for="(movie, index) in recommendList" :key="movie.id" :class="['carousel-item', { active: index === 0 }]">
                        <div class="carousel-caption d-none d-md-block">
                            <p>{{ movie.title }}</p>
                        </div>
                    </div>
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselAutoplaying" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselAutoplaying" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
            </div>
        </div> -->

        <!-- 데이터가 없는 경우 -->
        <!-- <div v-else>
            데이터가 없습니다.
        </div>
    </div>
</template>



<style scoped>
.loading-spinner {
    text-align: center;
    font-size: 1.5rem;
    margin-top: 20px;
}
.home-description{
       margin-top: 2rem; 
       font-weight: bold;
       display: flex;     
       flex-direction: column;
       align-items: center;
    }
.carousel-caption{
    font-size : 30px;
    font-weight : bold;
    color: white;
    text-align: left;
}
</style> --> -->
