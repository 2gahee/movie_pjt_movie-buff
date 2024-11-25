<template>
    <div>
        <div v-if="movieEvent.length">
            관련 이벤트
            <div v-for="event in movieEvent">
                <p>{{ event.goods_name }} <a href="https://www.megabox.co.kr/booking">(메가박스)</a></p>
                <div v-for="info in event.goods_info">
                    {{ info.region.split(" ")[0]}} - {{info.branch}} : {{ info.stock_status }}
                </div>
                
                
            </div>
        </div>
        <div v-else>
            확인된 이벤트 정보가 없습니다
        </div>
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
    // console.log(event.goods_name),
    // console.log(normalizeString(event.goods_name)),
    // console.log(normalizeString(props.title)),

    normalizeString(event.goods_name).includes(normalizeString(props.title))
    )})
</script>

<style scoped>

</style>