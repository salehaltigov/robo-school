<template>
  <VContainer
    class="about-school"
    id="about-school"
  >
    <VRow class="about-school__head pt-16 pb-15 ml-md-0 ml-5">
      <h2><b>Robo School</b> – учреждение для формирования кадрового
        <br> педагогического резерва в сфере робототехники
        <br> и программирования
      </h2>
    </VRow>
    <VRow class="about-school__body mb-15 text-md-start text-center">
      <VCol
        lg="3"
        md="4"
        sm="6"
        cols="12"
      >
        <h1>10</h1>
        <p>УМК по различным направлениям по робототехнике</p>
      </VCol>
      <VCol
        lg="3"
        md="4"
        sm="6"
        cols="12"
      >
        <h1>20</h1>
        <p>Школ, в которых запущена робототехника</p>
      </VCol>
      <VCol
        lg="3"
        md="4"
        sm="6"
        cols="12"
      >
        <h1>100</h1>
        <p>Педагогов прошедших курсы повышения квалификации</p>
      </VCol>
      <VCol
        lg="3"
        md="4"
        sm="6"
        cols="12"
      >
        <h1>10 000</h1>
        <p>Обученных детей на базе собственных центров</p>
      </VCol>
    </VRow>
  </VContainer>
  <div class="about-course__section">
    <VContainer class="mt-15">
      <VRow class="section-title mb-15 pt-16 d-flex justify-md-start justify-center text-center">
        <h1>Что вы получите после курса</h1>
      </VRow>
      <VRow class="about-course__body text-sm-start text-center mb-16">
        <VCol
          lg="4"
          md="4"
          sm="4"
          cols="12"
        >
          <h2 class="about-course__body-head">Удостоверение</h2>
          <p>Дающее право преподавать робототехнику для детей 6-12 лет в образовательных учреждениях</p>
        </VCol>
        <VCol
          lg="4"
          md="4"
          sm="4"
          cols="12"
        >
          <h2>Знания</h2>
          <p>По основам разработки учебно-методических комплексов по робототехнике и программированию</p>
        </VCol>
        <VCol
          lg="4"
          md="4"
          sm="4"
          cols="12"
        >
          <h2>Практику
            <VTooltip text="При наличии свободных мест">
              <template v-slot:activator="{ props }">
                <VIcon
                  size="small"
                  color="#141024"
                  icon="mdi-information-outline"
                  v-bind="props"
                >
                </VIcon>
              </template>
            </VTooltip>
          </h2>
          <p>Возможность пройти практику по преподаванию робототехники на базе R:ED LAB (в оффлайн или онлайн формате)</p>
        </VCol>
      </VRow>
    </VContainer>
  </div>
</template>

<script setup lang="ts">
</script>