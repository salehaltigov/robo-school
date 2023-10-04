<template>
  <VContainer
    class="trainers"
    id="trainers"
  >
    <VRow class="trainers__head">
      <h1>Профессиональные тренеры</h1>
    </VRow>
    <VCarousel
      hide-delimiters
      height="600"
    >
      <VCarouselItem
        v-for="trainer in trainersList"
        :key="trainer.id"
      >
        <TrainerCard :trainer="trainer" />
      </VCarouselItem>
    </VCarousel>
  </VContainer>
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