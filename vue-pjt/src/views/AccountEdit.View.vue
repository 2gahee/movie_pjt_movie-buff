<template>
    <div class="edit-profile-container">
        <div class="edit-card">
            <div class="edit-header">
                <h2>프로필 수정</h2>
                <router-link to="/mypage" class="back-button">
                    돌아가기
                </router-link>
            </div>

            <form @submit.prevent="handleSubmit" class="edit-form">
                <div class="form-section">
                    <div class="form-group">
                        <label for="nickname">닉네임</label>
                        <input 
                            id="nickname"
                            v-model="formData.nickname"
                            type="text"
                            :class="{ 'error': errors.nickname }"
                        />
                        <span v-if="errors.nickname" class="error-message">{{ errors.nickname }}</span>
                    </div>

                    <div class="form-group">
                        <label for="currentPassword">현재 비밀번호</label>
                        <input 
                            id="currentPassword"
                            v-model="formData.currentPassword"
                            type="password"
                            :class="{ 'error': errors.currentPassword }"
                        />
                        <span v-if="errors.currentPassword" class="error-message">{{ errors.currentPassword }}</span>
                    </div>

                    <div class="form-group">
                        <label for="newPassword">새 비밀번호</label>
                        <input 
                            id="newPassword"
                            v-model="formData.newPassword"
                            type="password"
                            :class="{ 'error': errors.newPassword }"
                        />
                        <span v-if="errors.newPassword" class="error-message">{{ errors.newPassword }}</span>
                    </div>

                    <div class="form-group">
                        <label for="confirmPassword">새 비밀번호 확인</label>
                        <input 
                            id="confirmPassword"
                            v-model="formData.confirmPassword"
                            type="password"
                            :class="{ 'error': errors.confirmPassword }"
                        />
                        <span v-if="errors.confirmPassword" class="error-message">{{ errors.confirmPassword }}</span>
                    </div>
                </div>

                <div class="form-actions">
                    <button 
                        type="submit" 
                        class="submit-button" 
                        :disabled="isSubmitting"
                    >
                        {{ isSubmitting ? '저장 중...' : '저장하기' }}
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import { useMovieStore } from '@/stores/counter';

const router = useRouter();
const store = useMovieStore();
const isSubmitting = ref(false);

const formData = reactive({
    nickname: '',
    currentPassword: '',
    newPassword: '',
    confirmPassword: ''
});

const errors = reactive({
    nickname: '',
    currentPassword: '',
    newPassword: '',
    confirmPassword: ''
});

const validateForm = () => {
    let isValid = true;
    // 에러 초기화
    Object.keys(errors).forEach(key => errors[key] = '');

    // 닉네임 검증
    if (!formData.nickname) {
        errors.nickname = '닉네임을 입력해주세요.';
        isValid = false;
    } else if (formData.nickname.length < 2) {
        errors.nickname = '닉네임은 2자 이상이어야 합니다.';
        isValid = false;
    }

    // 비밀번호 변경 시에만 검증
    if (formData.newPassword || formData.confirmPassword || formData.currentPassword) {
        if (!formData.currentPassword) {
            errors.currentPassword = '현재 비밀번호를 입력해주세요.';
            isValid = false;
        }

        if (!formData.newPassword) {
            errors.newPassword = '새 비밀번호를 입력해주세요.';
            isValid = false;
        } else if (formData.newPassword.length < 8) {
            errors.newPassword = '비밀번호는 8자 이상이어야 합니다.';
            isValid = false;
        }

        if (formData.newPassword !== formData.confirmPassword) {
            errors.confirmPassword = '비밀번호가 일치하지 않습니다.';
            isValid = false;
        }
    }

    return isValid;
};

// 폼 제출 함수
const handleSubmit = async () => {
    if (!validateForm()) return;
    
    try {
        isSubmitting.value = true;
        
        const updateData = {
            nickname: formData.nickname,
            ...(formData.newPassword && {
                currentPassword: formData.currentPassword,
                newPassword: formData.newPassword
            })
        };

          // store.updateUserProfile을 통해 서버에 요청 보내기
          const response = await store.updateUserProfile(updateData); // store가 API 요청 보내는 함수
        if (response.success) { // 서버에서 성공적으로 응답이 오면
            alert('회원정보가 수정되었습니다.');
            router.push('/mypage'); // 수정 후 마이페이지로 이동
        } else {
            // 응답에 따라 에러 메시지 표시
            if (response.errors) {
                Object.keys(response.errors).forEach(field => {
                    errors[field] = response.errors[field];
                });
            }
        }
    } catch (error) {
        console.error('Error updating profile:', error);
        // 에러 발생 시 처리
        alert('프로필 수정에 실패했습니다. 다시 시도해주세요.');
    } finally {
        isSubmitting.value = false;
    }
};
</script>

<style scoped>
.edit-profile-container {
    max-width: 600px;
    margin: 2rem auto;
    padding: 0 1rem;
}

.edit-card {
    background: white;
    border-radius: 16px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    overflow: hidden;
}

.edit-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem 2rem;
    border-bottom: 1px solid #eef0f5;
}

.edit-header h2 {
    font-size: 1.5rem;
    font-weight: 600;
    color: #2c3e50;
    margin: 0;
}

.back-button {
    padding: 0.6rem 1.2rem;
    background-color: #000;
    color: white;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 500;
    transition: background-color 0.2s;
}

.back-button:hover {
    background-color: #555;
}

.edit-form {
    padding: 2rem;
}

.form-section {
    display: grid;
    gap: 1.5rem;
    margin-bottom: 2rem;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.form-group label {
    font-size: 0.95rem;
    color: #4a5568;
    font-weight: 500;
}

.form-group input {
    padding: 0.75rem 1rem;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    font-size: 1rem;
    transition: all 0.2s;
}

.form-group input:focus {
    outline: none;
    border-color: #3498db;
    box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.2);
}

.form-group input.error {
    border-color: #e74c3c;
}

.error-message {
    font-size: 0.85rem;
    color: #e74c3c;
}

.form-actions {
    display: flex;
    justify-content: flex-end;
}

.submit-button {
    padding: 0.75rem 2rem;
    background-color: #000;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.2s;
}

.submit-button:hover:not(:disabled) {
    background-color: #555;
}

.submit-button:disabled {
    background-color: #a0aec0;
    cursor: not-allowed;
}

</style>