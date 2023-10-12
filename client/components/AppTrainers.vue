<template>
  <VContainer
    class="trainers mt-16"
    id="trainers"
  >
    <VRow class="section-title pb-15 mt-16 d-flex justify-md-start justify-center text-center">
      <h1>Профессиональные тренеры</h1>
    </VRow>
  </VContainer>
  <div class="trainers__slider">
    <VSlideGroup
      v-model="model"
      class="pa-4"
      prev-icon="mdi-chevron-left-circle"
      next-icon="mdi-chevron-right-circle"
      multiple
      lg-show-arrows
    >
      <VSlideGroupItem
        v-for="trainer in trainersList"
        :key="trainer.id"
      >
        <TrainerCard :trainer="trainer" />
      </VSlideGroupItem>
    </VSlideGroup>
  </div>
</template>

<script setup lang="ts">
import { TrainerModel } from 'models/base'
const { $api } = useNuxtApp()
const trainersList = ref<TrainerModel[]>([])
const getTrainers = async () => {
  trainersList.value = await $api<TrainerModel[]>('trainer/list/')
}

getTrainers()
</script>