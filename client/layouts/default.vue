<template>
  <VApp>
    <VAppBar
      class="app-bar"
      height="prominent"
      flat="false"
      text-color="#fff"
    >
      <div class="app-bar__content w-100">
        <VRow
          no-gutters
          class="app-bar__row pt-3 text-center align-center"
        >
          <VCol class="app-bar__logo d-flex">
            <a
              href=""
              class="pl-md-16 pl-sm-16 pl-7"
            >ROBO.SCHOOL</a>
          </VCol>
          <VCol class="app-bar__links d-flex align-center justify-center text-center">
            <a
              href="#about-school"
              class="mr-10  d-none d-sm-flex flex-row"
            >О школе </a>
            <a
              href="#trainers"
              class="mr-10  d-none d-sm-flex flex-row"
            >Тренеры </a>
            <a
              href="#price"
              class=" d-none d-sm-flex flex-row"
            >Стоимость</a>
          </VCol>
          <VCol class="app-bar__tel d-sm-flex justify-end d-none">
            <a
              href="tel:+78000001122"
              class="pr-16"
            >+7 800 000 11 22</a>
          </VCol>

          <VMenu class="d-inline d-sm-none">
            <template v-slot:activator="{ props }">
              <a href="tel:+78000001122">
                <VBtn
                  class="d-inline d-sm-none mr-2"
                  min-width="50"
                  min-height="50"
                  icon="true"
                >
                  <VImg
                    :src="phoneImg"
                    max-width="50"
                  >
                  </VImg>
                </VBtn>
              </a>
              <VBtn
                class="d-inline d-sm-none mr-2"
                v-bind="props"
                min-width="50"
                min-height="50"
                icon="true"
              >
                <VImg
                  :src="menuImg"
                  max-width="50"
                >

                </VImg>
              </VBtn>
            </template>
            <VList>
              <VListItem>
                <a href="#about-school">О школе</a>
              </VListItem>
              <VListItem>
                <a href="#trainers">Тренеры</a>
              </VListItem>
              <VListItem>
                <a href="#price">Стоимость</a>
              </VListItem>
            </VList>
          </VMenu>
        </VRow>
        <v-spacer />
      </div>
    </VAppBar>
    <VMain>
      <slot />
    </VMain>
    <Foooter />
  </VApp>
</template>

<script setup lang="ts">
// import rsueLogo from 'images/rsue_logo.svg'
import Foooter from './Footer.vue'
import menuImg from 'images/menu_img.svg'
import phoneImg from 'images/phone_img.png'
</script>
