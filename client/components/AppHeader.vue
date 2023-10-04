<template>
  <div class="main-header mb-16">
    <VRow
      no-gutters
      class="main-header__bar pt-3 text-center"
    >
      <VCol class="main-header__logo">
        <a href="">ROBO.SCHOOL</a>
      </VCol>
      <VCol class="main-header__links d-flex align-center justify-center text-center">
        <a
          href="#about-school"
          class="mr-10"
        >О школе </a>
        <a
          href="#trainers"
          class="mr-10"
        >Тренеры </a>
        <a href="#price">Стоимость</a>
      </VCol>
      <VCol class="main-header__tel">
        <a href="">+7 800 000 11 22</a>
      </VCol>
    </VRow>
    <VContainer class="main-header__body d-flex align-center">
      <VRow>
        <VCol>
          <h1 class="pb-5">ROBO SCHOOL</h1>
          <p>Курсы повышения квалификации по робототехнике <br> для педагогов начальной школы</p>
          <a
            href=""
            class="main-header__button d-inline-flex justify-center align-center text-center py-6 px-14 mt-13"
          >Записаться на курс</a>
        </VCol>
        <VCol>
          <VImg
            :src="mainImage"
            width="740"
            height="850"
            class="main-header__img"
          ></VImg>
        </VCol>
      </VRow>
    </VContainer>
  </div>
</template>

<script setup lang="ts">
import mainImage from 'images/main-image.png'
</script>