export interface TrainerSocialModel{
  readonly id: number
  icon: string
  link: string
}
export interface TrainerModel {
  readonly id: number
  firstname: string
  lastname: string
  img: string | null
  position: string
  text: string
  order: number | null
  social: TrainerSocialModel
}
