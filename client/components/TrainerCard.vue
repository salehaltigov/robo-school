<template>
  <VCard class="mr-md-10 mx-1">
    <VImg
      :width="360"
      :height="500"
      :src="trainer.img"
      cover
      class="trainers__img"
    >
    </VImg>
    <div class="pt-4 ml-4">
      {{ trainer.firstname }} {{ trainer.lastname }}
    </div>
    <VCardText>
      <div>{{ trainer.position }}</div>
      <VDialog
        width="940"
        height="664"
      >
        <template v-slot:activator="{ props }">
          <VBtn
            color="#D52027"
            class="text-none px-0 mt-5"
            variant="text"
            v-bind="props"
          >Подробнее
          </VBtn>
        </template>

        <template v-slot:default="{ isActive }">
          <VCard class="trainer-dialog">
            <VRow class="my-10 ml-10">
              <VCol class="pa-0 d-flex">
                <VImg
                  min-width="60px"
                  min-height="88px"
                  :width="auto"
                  :height="auto"
                  :src="trainer.img"
                >
                </VImg>
                <div class="trainer-dialog__head ml-10">
                  {{ trainer.firstname }} {{ trainer.lastname }}
                  <div class="trainer-dialog__position my-2">{{ trainer.position }}</div>
                  <div class="trainer-dialog__social">
                    <SocialLinks
                      v-for="social in trainer?.socials"
                      :key="social.id"
                      :link="social.link"
                      :icon="social.icon"
                    />
                  </div>
                </div>
              </VCol>
              <VCol class="d-sm-flex justify-end pa-0 mr-10 d-none">
                <VBtn
                  color="#D52027"
                  class="text-none px-0 mx-0"
                  variant="text"
                  @click="isActive.value = false"
                >Закрыть</VBtn>
              </VCol>
              <VCol class="d-sm-none justify-end pa-0 mr-10 d-flex">
                <VBtn
                  color="#D52027"
                  class="text-none px-0 mx-0"
                  variant="text"
                  @click="isActive.value = false"
                  icon="mdi-close"
                ></VBtn>
              </VCol>
            </VRow>
            <div class="trainer-dialog__text-info mb-5 ml-10">Информация</div>
            <p class="trainer-dialog__text-underline mb-5 mx-auto"></p>
            <div class="trainer-dialog__text mb-10 ml-10">{{ trainer.text }}</div>
          </VCard>
        </template>
      </VDialog>
    </VCardText>
  </VCard>
</template>

<script setup lang="ts">
import { TrainerModel } from 'models/base'
import { PropType } from 'vue'
import SocialLinks from './SocialLinks.vue'

defineProps({
  trainer: Object as PropType<TrainerModel>
})
</script>
