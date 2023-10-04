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
      <a href="">Подробнее</a>
    </VCardText>
  </VCard>
</template>

<script setup lang="ts">
import { TrainerModel } from 'models/base'
import { PropType } from 'vue'

defineProps({
  trainer: Object as PropType<TrainerModel>
})
</script>
