<template>
    
    <div class="event-box">
        <div v-if="movieEvent.length" class="event-title">
            관련 이벤트
            <div v-for="event in movieEvent" :key="event.goods_name">
                <p class="event-info">{{ event.name }} <a href="https://www.megabox.co.kr/booking">(메가박스)</a></p>
                {{ event[1] }}
                <div v-for="(info, name, index) in event.cinemas[1]" :key="name" class="event-details">
                    <!-- {{ info.region.split(" ")[0]}} - {{info.branch}} : {{ info.stock_status }} -->
                      <p v-if="name !== 'cinema'">{{ name }}점 - 재고 {{ info.stock }}, 약 {{ Math.round(info.time / 60) }}분 소요</p>
                </div>
            </div>
        </div>
        <div v-else class="event-title2">
            확인된 이벤트 정보가 없습니다
        </div>
        <div id="map" style="width:500px;height:400px;"></div>
        
    </div>
</template>


<script setup>
import { onMounted, computed } from 'vue';
const props = defineProps({
    title: String
})
const normalizeString = (str) => {
    return str
        .toLowerCase()                             // 대소문자 구분 없이 처리
        .replace(/\s+/g, ' ')                      // 여러 개의 공백을 하나로 변환
        .trim()                                    // 양옆 공백 제거
        .replace(/[^가-힣]/g, '')                  // 한글 외의 모든 문자(숫자, 기호 등) 제거
}

const eventList = JSON.parse(localStorage.getItem('megabox')) || []
console.log(eventList)
const movieEvent = computed(() => { 
    if (!props.title) {
        return []
    }
    return eventList.filter((event) => 
    event.name.includes(props.title)
    )})

// let container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
// let options = { //지도를 생성할 때 필요한 기본 옵션
// 	center: new kakao.maps.LatLng(33.450701, 126.570667), //지도의 중심좌표.
// 	level: 3 //지도의 레벨(확대, 축소 정도)
// };

// let map = new kakao.maps.Map(container, options)
</script>

<style scoped>
.event-box {
 margin-top: 2rem;
}
.event-title {
  font-style: italic;
  color: #666;
  margin-bottom: 1rem;
  font-size: 1.5rem;
}
.event-info {
  font-size: 1.2rem; 
  color: black; 
  margin: 0.5rem 0; 
}

.event-details {
  font-size: 0.9rem; 
  color: black; 
  margin-left: 1rem; 
}

.event-title2 {
  font-style: italic;
  color: #666;
  margin-bottom: 1rem;
  font-size: 1.2rem;
}
</style>