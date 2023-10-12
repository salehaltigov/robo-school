<template>
  <div class="main-header mb-16 pt-16">
    <VContainer class="main-header__body text-md-body-1 text-subtitle-2 pb-0">
      <VRow>
        <VCol
          lg="6"
          md="6"
          sm="12"
          cols="12"
          class="d-flex flex-column justify-md-center justify-start align-md-start align-center text-md-start text-center"
        >
          <h1 class="main-header__name pb-5 text-md-h2 text-h4 mt-md-0 mt-16">ROBO SCHOOL</h1>
          <p>Курсы повышения квалификации по робототехнике <br> для педагогов начальной школы</p>
          <a
            href="#feedback"
            class="main-header__button d-md-inline-flex justify-center align-center text-center py-6 px-13 mt-13 text-md-body-1 text-subtitle-2 d-none"
          >Записаться на курс</a>
        </VCol>
        <VCol
          lg="6"
          md="6"
          sm="12"
          cols="12"
          class="d-flex flex-column justify-center align-center pb-0"
        >
          <VImg
            :src="mainImage"
            width="780"
            height="883"
            max-width="780"
            max-height="883"
            class="main-header__img"
          ></VImg>
          <a
            href="#feedback"
            class="main-header__button d-md-none justify-center align-center text-center py-6 px-13 text-md-body-1 text-subtitle-2 d-inline-flex mb-10"
          >Записаться на курс</a>
        </VCol>
      </VRow>
    </VContainer>
  </div>
</template>

<script setup lang="ts">
import mainImage from 'images/main-image.png'
</script>