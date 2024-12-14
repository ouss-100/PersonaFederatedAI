"use server"
import ECommerce from "@/components/Dashboard/E-commerce";
import { Metadata } from "next";
import DefaultLayout from "@/components/Layouts/DefaultLayout";
import { getFiveUsers, getTopPersonalitiesForChart, getUserMetrics, getUserPersonalityDistribution } from "./actions/User";

export default async function Home() {
  const result = await getUserMetrics();
  const personalityDistribution = await getUserPersonalityDistribution(5)
  const fiveUsers = await getFiveUsers() || []
  const topPerso = await getTopPersonalitiesForChart()
  return (
    <>
      <DefaultLayout>
        <ECommerce metrics={result} personalityDistribution={personalityDistribution} fiveUsers={fiveUsers} topPerso={topPerso} />
      </DefaultLayout>
    </>
  );
}
