import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

// Function to generate random percentages summing to 100 for the five personalities
function generatePersonalityValues() {
  // Generate random values for 5 personalities
  const value1 = Math.random() * 100;
  const value2 = Math.random() * (100 - value1);
  const value3 = Math.random() * (100 - value1 - value2);
  const value4 = Math.random() * (100 - value1 - value2 - value3);
  const value5 = 100 - (value1 + value2 + value3 + value4);

  // Shuffle the values to make them random
  const values = [value1, value2, value3, value4, value5];
  values.sort(() => Math.random() - 0.5);

  return [
    { name: "Openness", value: values[0] },
    { name: "Conscientiousness", value: values[1] },
    { name: "Agreeableness", value: values[2] },
    { name: "Extraversion", value: values[3] },
    { name: "Neuroticism", value: values[4] },
  ];
}

// Dummy user data
const users = [
  {
    email: "med.mouhib@example.com",
    name: "Med Mouhib",
    dominantpersonality: "Extraversion",
  },
  {
    email: "sofia.karoui@example.com",
    name: "Sofia Karoui",
    dominantpersonality: "Openness",
  },
  {
    email: "ali.benhassen@example.com",
    name: "Ali Ben Hassen",
    dominantpersonality: "Conscientiousness",
  },
  {
    email: "amira.chaouachi@example.com",
    name: "Amira Chaouachi",
    dominantpersonality: "Agreeableness",
  },
  {
    email: "khaled.zied@example.com",
    name: "Khaled Zied",
    dominantpersonality: "Neuroticism",
  },
];

async function seed() {
  try {
    // Start seeding users
    for (const userData of users) {
      const personalities = generatePersonalityValues();

      const user = await prisma.user.create({
        data: {
          email: userData.email,
          name: userData.name,
          dominantpersonality: userData.dominantpersonality,
          userpersonality: {
            create: personalities.map((personality) => ({
              name: personality.name,
              value: personality.value,
            })),
          },
        },
      });

      console.log(`User created: ${user.name} (ID: ${user.id})`);
    }
  } catch (error) {
    console.error("Error seeding database:", error);
  } finally {
    await prisma.$disconnect();
  }
}

seed();
