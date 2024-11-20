
<template>
    <div>
        <section class="bg">
        <div class="container py-4">
            <div class="row align-items-center justify-content-between">
                <a class="navbar-brand h1 text-center" href="index.do">
                    <span class="text-dark h4">Accounts</span>                 
                </a>
            </div>
            <form @submit.prevent="signUp">
                <div class="form-group">
               		<label for="inputUsername" class="form-label mt-4">아이디</label>
                    <input type="text" class="form-control" id="inputUsername" v-model.trim="username">
                </div>

                <div class="form-group">
               		<label for="inputEmail" class="form-label mt-4">이메일</label>
                    <input type="email" class="form-control" id="inputEmail" v-model.trim="email" placeholder="선택입력">
                </div>


                <div class="form-group">
               		<label for="inputNickname" class="form-label mt-4">닉네임</label>
                    <input type="text" class="form-control" id="inputNickname" v-model.trim="nickname">
                </div>

				 <!-- <div class="form-group has-success">
					<label class="form-label mt-4" for="inputValid">비밀번호</label>
					<input type="password" class="form-control is-valid" id="inputValid">
					<div class="valid-feedback"></div>
				</div> -->


                <div :class="['form-group', passwordValid ? 'has-success' : '']">
                    <label class="form-label mt-4" for="password1">비밀번호</label>
                    <input
                    type="password"
                    class="form-control"
                    :class="{ 'is-valid': passwordValid }"
                    id="password1"
                    v-model.trim="password1"
                    />
                    <div class="valid-feedback" v-if="passwordValid">비밀번호 입력 완료</div>
                </div>


                <!-- <div class="form-group has-danger">
					<label class="form-label mt-4" for="inputInvalid">비밀번호 재확인</label> 
					<input type="password" class="form-control is-invalid" id="inputInvalid">
					<div class="invalid-feedback">비밀번호가 일치하지 않습니다</div>
				</div>  -->

                <div :class="['form-group', passwordMatch ? 'has-success' : 'has-danger']">
                    <label class="form-label mt-4" for="password2">비밀번호 재확인</label>
                    <input
                    type="password"
                    class="form-control"
                    :class="{ 'is-invalid': !passwordMatch && password2, 'is-valid': passwordMatch }"
                    id="password2"
                    v-model.trim="password2"
                    />
                    <div class="valid-feedback" v-if="passwordMatch">비밀번호가 일치합니다</div>
                    <div class="invalid-feedback" v-else-if="password2">비밀번호가 일치하지 않습니다</div>
                </div>


				<div class="d-grid gap-2">
                    <button class="btn btn-primary btn-lg" type="submit" :disabled="!formValid">가입하기</button>
                </div>
            </form>
        </div>
    </section>

    </div>
</template>

<script setup>
import {useRouter } from 'vue-router'
import { ref, computed } from 'vue';
import { useMovieStore } from '@/stores/counter'

const router = useRouter();

const username = ref('');
const email = ref('');
const nickname = ref('');
const password1 =ref('');
const password2 =ref('');

const store = useMovieStore()

const signUp = function () {
//   console.log('signUp메서드 호출됨');  
  const payload = {
    username: username.value,
    email: email.value,
    nickname : nickname.value,
    password1: password1.value,
    password2: password2.value,
  }
  store.signUp(payload)
}


const passwordValid = computed(() => password1.value.length >= 6);
const passwordMatch = computed(() => password1.value === password2.value);
const allFieldsFilled = computed(() =>
  username.value.trim() &&
  nickname.value.trim() &&
  password1.value.trim() &&
  password2.value.trim()
);
const formValid = computed(() => passwordValid.value && passwordMatch.value && allFieldsFilled.value)

</script>

<style scoped>
.bg{
		height: 1053px;
		padding-top:55px;
		padding-bottom:75px;
	}
	.flex-fill.mx-xl-5.mb-2{
		margin: 0 auto;
		width : 700px;
		padding-right: 7rem;
		padding-left: 7rem;
	}
    /* <!-- 입력창 --> */
	.container.py-4{
		margin: 0 auto;
		width : 503px;
	}
    /* <!-- 가입하기 --> */
	.d-grid.gap-2{
		padding-top: 30px;
	}
</style>