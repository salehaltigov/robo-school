<template>
  <a
    :href="link"
    target="_blank"
    :class="customClass"
    class="social-link"
  >
    <VIcon
      class="mr-2"
      :icon="'mdi ' + icon"
      :size="iconSize"
    />
  </a>
</template>

<script setup lang="ts">
defineProps({
  link: String,
  icon: String,
  iconSize: String,
  customClass: String
})
</script>