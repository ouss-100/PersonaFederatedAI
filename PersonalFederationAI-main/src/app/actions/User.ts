"use server"
import prisma from "../utils/prismaclient"

export async function getUserMetrics() {
    const currentDate = new Date();
  
    const startOfCurrentMonth = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1);
  
    const startOfPreviousMonth = new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1);
  
    const totalUsers = await prisma.user.count();
  
    const usersThisMonth = await prisma.user.count({
      where: {
        createdAt: {
          gte: startOfCurrentMonth,
        },
      },
    });
  
    const usersLastMonth = await prisma.user.count({
      where: {
        createdAt: {
          gte: startOfPreviousMonth,
          lt: startOfCurrentMonth,
        },
      },
    });
  
    const growthPercentage = usersLastMonth === 0 
      ? (usersThisMonth > 0 ? 100 : 0) 
      : ((usersThisMonth - usersLastMonth) / usersLastMonth) * 100;
  
    const personalityResult = await prisma.userPersonality.groupBy({
      by: ['name'],
      _count: {
        name: true,
      },
      orderBy: {
        _count: {
          name: 'desc',
        },
      },
      take: 1,
    });
  
    let mostCommonPersonality = null;
    if (personalityResult.length > 0) {
      const mostCommon = personalityResult[0];
      const percentage = ((mostCommon._count.name / totalUsers) * 100).toFixed(2);
      mostCommonPersonality = {
        name: mostCommon.name,
        percentage: `${percentage}%`
      };
    }
  
    return {
      userMetrics: {
        userCountThisMonth: usersThisMonth,
        growthPercentage: growthPercentage.toFixed(2),
      },
      totalUsers,
      mostCommonPersonality,
    };
}


export async function getUserPersonalityDistribution(userId: number) {
    const orderedLabels = ["Neuroticism", "Agreeableness", "Extraversion", "Conscientiousness", "Openness"];
    const personalities = await prisma.userPersonality.findMany({
        where: { userId },
        select: {
        name: true,
        value: true,
        },
    });

    if (personalities.length === 0) {
        return null;
    }

    const distributionMap = Object.fromEntries(
        personalities.map(personality => [personality.name, personality.value])
    );

    const series = orderedLabels.map(label => distributionMap[label] || 0);
    return series;
}

export async function getFiveUsers() {
    const users = await prisma.user.findMany({
      take: 5,
      select: {
        id: true,
        email: true,
        name: true,
        dominantpersonality: true,
        createdAt: true,
      },
    });
  
    return users;
}

export const getTopPersonalitiesForChart = async () => {
    const users = await prisma.user.findMany({
      include: {
        userpersonality: {
          select: {
            name: true,
            value: true,
          },
          orderBy: {
            value: 'desc', 
          },
          take: 2, 
        },
      },
    });
  
    const series: any[] = [];
  
    users.forEach(user => {
      user.userpersonality.forEach((personality, index) => {
        if (!series[index]) {
          series[index] = {
            name: personality.name,
            data: [],
          };
        }
  
        series[index].data.push(personality.value.toFixed(2));
      });
    });
  
    return series;
};