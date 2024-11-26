<!-- <template>
  <div>
      <h1>LogIn Page</h1>
      <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model.trim="username"><br>
  
      <label for="password">password : </label>
      <input type="password" id="password" v-model.trim="password"><br>
  
      <input  type="submit" value="logIn">
      </form>
  </div>
  </template> -->

  <template>
    <div>
      <section class="bg-login">
        <div class="container py-5">
          <div class="row justify-content-center">
            <div class="col-md-6 col-lg-4">
              <div class="card shadow-lg">
                <div class="card-body">
                  <h3 class="card-title text-center mb-4">로그인</h3>
                  <form @submit.prevent="logIn">
                    <!-- 아이디 입력 -->
                    <div class="form-group">
                      <label for="inputUsername" class="form-label mt-4">아이디</label>
                      <input
                        type="text"
                        class="form-control"
                        id="inputUsername"
                        v-model.trim="username"
                        placeholder="아이디를 입력하세요"
                      />
                    </div>
  
                    <!-- 비밀번호 입력 -->
                    <div class="form-group">
                      <label for="inputPassword" class="form-label mt-4">비밀번호</label>
                      <input
                        type="password"
                        class="form-control"
                        id="inputPassword"
                        v-model.trim="password"
                        placeholder="비밀번호를 입력하세요"
                      />
                    </div>
  
                    <!-- 로그인 버튼 -->
                    <div class="d-grid gap-2 mt-4">
                      <button class="btn btn-primary btn-lg" type="submit">
                        로그인
                      </button>
                    </div>
  
                    <!-- 회원가입 링크 -->
                    <div class="mt-3 text-center">
                      <a href="/signup" class="text-decoration-none">회원가입</a>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </template>
  
<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/counter'

const username = ref(null)
const password = ref(null)

const store = useMovieStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

</script>

<style scoped>


.card {
  border-radius: 8px;
}

.card-body {
  padding: 2rem;
}

.card-title {
  font-size: 1.5rem;
  font-weight: bold;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-label {
  font-weight: 600;
}

.input-group input {
  font-size: 1rem;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
}

.btn-primary:hover {
  background-color: #0056b3;
  border-color: #0056b3;
}

.text-center a {
  color: #007bff;
}

.text-center a:hover {
  text-decoration: underline;
}

.d-grid {
  display: grid;
  gap: 1rem;
}
</style>