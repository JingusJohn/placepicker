import { Inter } from '@next/font/google'
import ModeSwitcher from '@/components/ModeSwitcher';

const inter = Inter({ subsets: ['latin'] })



export default function Home() {
  return (
    <ModeSwitcher mode={"FilteredRandom"} withData={true} />
  )
}
