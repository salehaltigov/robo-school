<template>
  <VCard>
    <VImg
      :width="300"
      :src="trainer.img"
    >
    </VImg>
    <VCardSubtitle class="pt-4">
      {{ trainer.firstname }} {{ trainer.lastname }}
    </VCardSubtitle>
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
