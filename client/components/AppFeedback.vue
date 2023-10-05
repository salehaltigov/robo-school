<template>
  <div class="feedback py-16 mt-16">
    <VContainer>
      <VRow class="d-flex justify-center align-center mx-auto">
        <VCol class="feedback__text">
          <h2 class="feedback__text-head mb-5">Запишитесь на курс <br> со скидкой 10%</h2>
          <p>Акция действительна до 10 марта 2022 года</p>
        </VCol>
        <VCol>
          <VTextField
            v-model="state.firstname"
            :error-messages="v$.firstname.$errors.map(e => e.$message)"
            required
            single-line
            bg-color="#FFD5BB"
            placeholder="Имя"
          ></VTextField>
          <VTextField
            v-model="state.phone"
            :error-messages="v$.phone.$errors.map(e => e.$message)"
            required
            single-line
            bg-color="#FFD5BB"
            placeholder="Телефон"
          ></VTextField>
          <VTextField
            v-model="state.email"
            :error-messages="v$.email.$errors.map(e => e.$message)"
            required
            single-line
            bg-color="#FFD5BB"
            placeholder="E-mail"
          ></VTextField>
          <VBtn
            @click="handleSubmit"
            block
            class="feedback__form-btn mt-2"
            rounded="0"
          >Оформить заявку</VBtn>
        </VCol>
      </VRow>
    </VContainer>
  </div>
</template>


<script setup lang="ts">
import { reactive, ref } from 'vue'
import { useVuelidate } from '@vuelidate/core'
import { email, required, helpers } from '@vuelidate/validators'
import type { FeedbackModel } from 'models/base'

const { $api } = useNuxtApp()

const initialState = {
  firstname: '',
  phone: '',
  email: '',
}

const state = reactive({
  ...initialState,
})

const rules = {
  firstname: { required: helpers.withMessage('Это обязательное поле', required) },
  phone: { required: helpers.withMessage('Это обязательное поле', required) },
  email: { required: helpers.withMessage('Это обязательное поле', required), email: helpers.withMessage('Пожалуйста, введите действительный адрес эл. почты', email) },
}

const v$ = useVuelidate(rules, state)

const handleSubmit = async () => {
  const isFormCorrect = await v$.value.$validate()

  if (isFormCorrect === false)
    return

  const data = {
    name: state.firstname,
    tel: state.phone,
    email: state.email,
  }
  await $api('/feedback/create/', { method: 'POST', body: data })
  v$.value.$reset()
  state.firstname = ''
  state.phone = ''
  state.email = ''
}
</script>