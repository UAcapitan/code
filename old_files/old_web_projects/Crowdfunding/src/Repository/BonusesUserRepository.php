<?php

namespace App\Repository;

use App\Entity\BonusesUser;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\Persistence\ManagerRegistry;

/**
 * @method BonusesUser|null find($id, $lockMode = null, $lockVersion = null)
 * @method BonusesUser|null findOneBy(array $criteria, array $orderBy = null)
 * @method BonusesUser[]    findAll()
 * @method BonusesUser[]    findBy(array $criteria, array $orderBy = null, $limit = null, $offset = null)
 */
class BonusesUserRepository extends ServiceEntityRepository
{
    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, BonusesUser::class);
    }

    // /**
    //  * @return BonusesUser[] Returns an array of BonusesUser objects
    //  */
    /*
    public function findByExampleField($value)
    {
        return $this->createQueryBuilder('b')
            ->andWhere('b.exampleField = :val')
            ->setParameter('val', $value)
            ->orderBy('b.id', 'ASC')
            ->setMaxResults(10)
            ->getQuery()
            ->getResult()
        ;
    }
    */

    /*
    public function findOneBySomeField($value): ?BonusesUser
    {
        return $this->createQueryBuilder('b')
            ->andWhere('b.exampleField = :val')
            ->setParameter('val', $value)
            ->getQuery()
            ->getOneOrNullResult()
        ;
    }
    */
}
