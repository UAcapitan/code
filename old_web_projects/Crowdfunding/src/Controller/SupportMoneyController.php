<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use App\Entity\Bonuses;
use App\Entity\BonusesUser;

class SupportMoneyController extends AbstractController
{
    /**
     * @Route("/support/{id}", name="support_money")
     */
    public function index(int $id): Response
    {

        $bonus = $this->getDoctrine()->getRepository(Bonuses::class)->find($id);

        $entityManager = $this->getDoctrine()->getManager();

        $campaign = $bonus->getCampaign();
        $campaign->setNowMoney($campaign->getNowMoney() + $bonus->getMoney());

        $bonusUser = new BonusesUser();

        $bonusUser->setName($bonus->getName());
        $bonusUser->setMoney($bonus->getMoney());
        $bonusUser->setDescription($bonus->getDescription());
        $bonusUser->setCampaign($bonus->getCampaign());
        $bonusUser->setUser($this->getUser());

        $entityManager->persist($campaign);
        $entityManager->persist($bonusUser);
        $entityManager->flush();

        return $this->render('support_money/index.html.twig', [
            'bonus' => $bonus,
            'campaign' => $campaign,
        ]);
    }
}
