    <template>
        <div class="home-description">
            <img src="/images/recommendlogo.png" alt="로고" class="recommendlogo" />
            <p>아래 버튼을 누르면 굿즈 재고를 기반으로 영화를 추천드려요!</p>
            <button class="btn btn-lg" @click.prevent="goodsRecommend">UPDATE</button> 
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
/* .carousel {
  width: 80%; 
  height: 40rem;
  margin: 0 auto; 
  margin-bottom: 5rem;
}
.carousel-item img {
  width: 100%; 
  height:40rem; 
  object-fit: cover; 
} */

.btn {
    background-color: #D72323;
    box-shadow: 0 0 0 1px #c63702 inset,
    0 0 0 2px rgba(255,255,255,0.15) inset,
    0 8px 0 0 #C24032,
    0 8px 0 1px rgba(0,0,0,0.4),
    0 8px 8px 1px rgba(0,0,0,0.5);
    margin-bottom: 2rem;
    width: 7rem;
    height: 2.5rem;
    text-align: center;
    color: #fff;
    text-shadow: -1px 0px #000, 0px 1px #000, 1px 0px #000, 0px -1px #000;
}
.btn:active {
    background-color: #B71C1C; 
    box-shadow: 0 0 0 1px #a61b1b inset, 
                0 0 0 2px #d7242426 inset,
                0 4px 0 0 #C24032,
                0 4px 4px 1px rgba(0,0,0,0.4);  
}
.recommendlogo {
  width: 10rem;
  height: auto; 
}
</style>