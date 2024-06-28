<template>
    <main class="size-full flex flex-col justify-center items-center">
        <div class="card bg-base-100 w-full max-w-sm shrink-0">
            <div class="card-body">
                <h1 class="form-control text-4xl text-center font-bold mb-4">
                    Carhyme Demo
                </h1>
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Username</span>
                    </label>
                    <input type="text" placeholder="Username" class="input input-bordered" required v-model="username" />
                </div>
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Password</span>
                    </label>
                    <input type="password" placeholder="password" class="input input-bordered" required v-model="password"/>
                    <label class="label">
                        <a href="#" class="label-text-alt link link-hover">Forgot password?</a>
                    </label>
                </div>
                <div class="form-control mt-6">
                    <button class="btn btn-primary" @click="login" >Login</button>
                </div>
            </div>
        </div>
    </main>

</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const username = ref<string>('');
const password = ref<string>('');

async function login(){
    const res = await $fetch('http://127.0.0.1:8000/api/token/pair', {
            method: 'POST',
            body: {
            username: username.value,
            password: password.value
            }
        });
    const token = useCookie('token')
    token.value = res.access
    router.push('/');
}
</script>
