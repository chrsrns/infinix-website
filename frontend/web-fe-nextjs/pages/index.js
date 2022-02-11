import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.scss'
import Container from 'react-bootstrap/Container'
import MasterHome from '../components/MasterHome'

export default function Home() {
  return (
    <div>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <MasterHome/>
      
    </div>
  )
}