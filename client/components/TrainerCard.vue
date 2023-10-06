<template>
  <VCard class="mr-10">
    <VImg
      :width="360"
      :height="500"
      :src="trainer.img"
      cover
    >
    </VImg>
    <div class="pt-4 ml-4">
      {{ trainer.firstname }} {{ trainer.lastname }}
    </div>
    <VCardText>
      <div>{{ trainer.position }}</div>
      <v-dialog
        width="940"
        height="664"
      >
        <template v-slot:activator="{ props }">
          <v-btn
            color="#D52027"
            class="text-none px-0 mt-5"
            variant="text"
            v-bind="props"
          >Подробнее
          </v-btn>
        </template>

        <template v-slot:default="{ isActive }">
          <VCard class="trainer-dialog">
            <VRow class="my-10 ml-10">
              <VCol class="pa-0 d-flex">
                <VImg
                  :width="160"
                  :height="222"
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
              <VCol class="d-flex justify-end pa-0 mr-10">
                <v-btn
                  color="#D52027"
                  class="text-none px-0 mx-0"
                  variant="text"
                  @click="isActive.value = false"
                >Закрыть</v-btn>
              </VCol>
            </VRow>
            <div class="trainer-dialog__text-head mb-5 ml-10">Информация</div>
            <p class="trainer-dialog__text-underline mb-5 mx-auto"></p>
            <div class="trainer-dialog__text mb-10 ml-10">{{ trainer.text }}</div>
          </VCard>
        </template>
      </v-dialog>
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
