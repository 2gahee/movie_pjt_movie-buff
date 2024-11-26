    <template>
        <div class="home-description">
            <img src="/images/recommendlogo.png" alt="로고" class="recommendlogo" />
            
            <p>{{ (isPressed && !eventMovies.length) ? "지점 별 굿즈 재고 정보를 수집중입니다..." : "아래 버튼을 누르면 다른 방식으로 영화를 추천드려요!" }}</p>
            
            
            <div v-if="isLoading">
            Loading movies...
            </div>
            <div v-else-if="bestRecommend" id="carouselAutoplaying" class="carousel slide" data-bs-ride="carousel">
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
            <div class="updatebutton-container" style="display: flex; justify-content: center;">
                <button class="btn btn-lg" @click.prevent="toggleEvent">{{ showEvent ? "상영 중인 영화" : "이벤트 중인 영화" }}</button>
            </div>
        </div>
        
    </template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useMovieStore } from '@/stores/counter';
import { useRouter } from 'vue-router'

const router = useRouter();
const store = useMovieStore()
const eventMovies = ref([])
const showEvent = ref(false)
const isLoading = ref(true)
const isPressed = ref(null)
// Fetch movies on component mount
onMounted(async () => {
    try {
        console.log("Fetching now-on movies...");
        await store.getNowOns(); // 데이터 로드
        isLoading.value = false;

        // 디버깅: 데이터 확인
        console.log("nowOns:", store.nowOns.value);
        console.log("wholeRecommendList:", wholeRecommendList.value);
        console.log("recommendList:", recommendList.value);
    } catch (error) {
        console.error("Failed to get now-on movies:", error);
        isLoading.value = false;
    }
})

const wholeRecommendList = computed(() => {
    // When show event is true and event movies exist, use event movies
    if (showEvent.value && eventMovies.value.length) {
        return eventMovies.value
    }
    // Otherwise use now on movies from the store
    return store.nowOns || []
})

const bestRecommend = computed(() => {
    const list = wholeRecommendList.value
    return list.length ? list[0] : null
})

const recommendList = computed(() => {
    const list = wholeRecommendList.value
    return list.length > 1 ? list.slice(1, 5) : []
})

const watchDetail = function(id) {
    router.push({name:'detail', params: {id}})
}

const imgString = function(movie) {
    return movie ? `https://image.tmdb.org/t/p/original${movie.backdrop_path}` : ''
}

const toggleEvent = async function() {
    try {
        // If switching to event movies and no event movies yet, fetch them
        isPressed.value = true
        if (!showEvent.value) {
            if (!eventMovies.value.length) {
                await goodsRecommend()
            }
        }
        
        // Toggle the show event flag
        showEvent.value = !showEvent.value
    } catch (error) {
        console.error('Error in toggleEvent:', error)
    }
}

const goodsRecommend = async function() {
    try {
        // First, log the events
        await store.getEvents()
        console.log('Events list:', store.eventList)

        if (store.eventList && store.eventList.length) {
            localStorage.setItem("megabox", JSON.stringify(store.eventList))
            
            // Log the first event's details
            console.log('First event:', store.eventList[0])
            console.log('First event cinemas:', store.eventList[0].cinemas)

            // Ensure the first cinema exists before accessing it
            if (!store.eventList[0].cinemas || !store.eventList[0].cinemas.length) {
                console.error('No cinemas found in the event')
                return
            }

            eventMovies.value = await Promise.all(store.eventList.map(async (event) => {
                // Ensure the event has cinemas
                if (!event.cinemas || !event.cinemas.length) {
                    console.error('Event without cinemas:', event)
                    return null
                }

                // Safer title extraction
                const title = Object.keys(event.cinemas[0])
                    .filter(key => !isNaN(key))
                    .sort((a, b) => a - b)
                    .map(key => event.cinemas[0][key])
                    .join("")

                console.log('Extracted title:', title)

                try {
                    const movies = await store.searchMovies(title)
                    console.log('Search movies result:', movies)

                    if (movies && Array.isArray(movies)) {
                        const movie = movies.find((movie) => movie.title === title)
                        console.log('Found movie:', movie)
                        return movie || null
                    } else {
                        console.error('Invalid movies response:', movies)
                        return null
                    }
                } catch (searchError) {
                    console.error('Error searching movies:', searchError)
                    return null
                }
            }))
            eventMovies.value = eventMovies.value.filter(movies => movies != null)
            console.log('Final eventMovies:', eventMovies.value)
        } else {
            console.error('No events found')
        }
    } catch (error) {
        console.error('Error in goodsRecommend:', error)
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
    text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7); 
}
.carousel {
  width: 95%; 
  height: 40rem;
  margin: 0 auto; 
  margin-bottom: 1rem;
}
.carousel-item img {
  width: 100%; 
  height:40rem; 
  object-fit: cover; 
}

.btn {
    background-color: #D72323;
    box-shadow: 0 0 0 1px #c63702 inset,
    0 0 0 2px rgba(255,255,255,0.15) inset,
    0 8px 0 0 #C24032,
    0 8px 0 1px rgba(0,0,0,0.4),
    0 8px 8px 1px rgba(0,0,0,0.5);
    margin-bottom: 2rem;
    width: 12rem;
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